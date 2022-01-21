import os
import json
import numpy as np
import argparse


def read_json(fpath):
    with open(fpath, 'r') as f:
        obj = json.load(f)
    return obj


def main(groundtruth_filename, ranking_results_filename):

    grountruth = read_json(groundtruth_filename)
    ranking_results = read_json(ranking_results_filename)

    queries_gt = grountruth["query"]
    galleries_gt = grountruth["gallery"]

    # action2gidx dict maps each action_idx to a list of gallery_idx from that action
    action2gidx = {}
    for gallery in galleries_gt.values():
        action_idx = gallery["action_idx"]
        if action_idx not in action2gidx:
            action2gidx[action_idx] = []
        action2gidx[action_idx].append(gallery["bbox_idx"])

    all_cmc = []
    all_AP = []
    max_rank = 1

    for q_idx in queries_gt.keys():
        query_gt = queries_gt[q_idx]
        q_pid = query_gt["person_uid"]
        q_action_idx = query_gt["action_idx"]

        if q_idx not in ranking_results:
            raise ValueError("No ranking provided for query '{}'. Make sure to provide ranking result for all queries.".format(q_idx))

        seen_galleries = set()
        gallery_ranking_idx = ranking_results[q_idx]
        gallery_ranking_pid = []
        for g_idx in gallery_ranking_idx:
            if not isinstance(g_idx, int):
                raise TypeError("Incorrect ranking result for query '{}'. Ranking must contain integer values only but contained '{}' of type '{}'".format(q_idx, g_idx, type(g_idx)))
            if g_idx in seen_galleries:
                raise ValueError("Gallery sample '{}' is referenced more than once in ranking result of query '{}'. "
                                 "Each gallery sample from the same action as the query must appear no more and not less than once in the ranking.".format(g_idx, q_idx))
            else:
                seen_galleries.add(g_idx)
            gallery_gt = galleries_gt[str(g_idx)]
            g_action_idx = gallery_gt["action_idx"]
            if q_action_idx != g_action_idx:
                raise ValueError("Ranking result for query '{}' from action '{}' contained gallery sample '{}' from a different action '{}'. "
                                 "Ranking results for a given query must contain only gallery samples from the same action.".format(q_idx, q_action_idx, g_idx, g_action_idx))
            gallery_ranking_pid.append(gallery_gt["person_uid"])

        # make sure all gallery samples are provided for given query
        gallery_ranking_idx_set = set(gallery_ranking_idx)
        for g_idx in action2gidx[q_action_idx]:
            if g_idx not in gallery_ranking_idx_set:
                raise ValueError("Ranking result for query '{}' is incorrect: missing gallery sample '{}' from same action '{}'. "
                                 "A gallery sample from the same action as the query should be listed in the ranking.".format(q_idx, g_idx, q_action_idx))

        matches = []
        for g_pid in gallery_ranking_pid:
            matches.append(g_pid == q_pid)

        raw_cmc = np.array(matches)
        if not np.any(raw_cmc):
            # this condition is true when query identity does not appear in gallery
            raise ValueError("Person id for query '{}' does not appear in gallery".format(q_idx))

        cmc1 = raw_cmc.cumsum()
        cmc1[cmc1 > 1] = 1
        cmc1 = cmc1[:max_rank]
        all_cmc.append(cmc1)

        # compute average precision
        # reference: https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Average_precision
        num_rel = raw_cmc.sum()
        tmp_cmc = raw_cmc.cumsum()
        tmp_cmc = [x / (i1 + 1.) for i1, x in enumerate(tmp_cmc)]
        tmp_cmc = np.asarray(tmp_cmc) * raw_cmc
        AP = tmp_cmc.sum() / num_rel
        all_AP.append(AP)

    all_cmc = np.asarray(all_cmc).astype(np.float32)
    all_cmc = all_cmc.sum(0) / len(queries_gt.keys())
    ap = np.mean(all_AP)
    result = all_cmc, ap
    cmc, mAP = result

    print('** Results **')
    print('filename: {}'.format(os.path.basename(ranking_results_filename)))
    print('mAP: {:.1%}'.format(mAP))
    ranks = [1]
    for r in ranks:
        print('Rank-{:<3}: {:.1%}'.format(r, cmc[r - 1]))

    performance_metrics = {}
    performance_metrics["mAP"] = mAP
    performance_metrics["rank-1"] = cmc[0]

    return performance_metrics


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-rs", "--ranking_results",
                        help="ranking result",
                        type=str,
                        default="")
    parser.add_argument("-gt", "--groundtruth",
                        help="groundtruth identities",
                        type=str,
                        default="")
    parsed_args = parser.parse_args()

    main(parsed_args.groundtruth, parsed_args.ranking_results)
