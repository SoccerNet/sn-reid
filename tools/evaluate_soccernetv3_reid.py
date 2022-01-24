import argparse

from SoccerNet.Evaluation.ReIdentification import evaluate

if __name__ == '__main__':

    # Load the arguments
    parser = argparse.ArgumentParser(description='Evaluation camera calibration task')

    parser.add_argument("-rs", "--ranking_results", required=True, type=str,
                        help='ranking result')
    parser.add_argument("-gt", "--groundtruth", required=True, type=str,
                        help="groundtruth identities")
    args = parser.parse_args()

    # Evaluate
    print(evaluate(args.groundtruth, args.ranking_results))

# Usage:
# python tools/EvaluateReIdentification.py -rs ranking_results_valid.json -gt path/to/SoccerNet/reid/valid/bbox_info.json
