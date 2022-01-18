from __future__ import division, print_function, absolute_import
import glob
import os
import os.path as osp
from torchreid.utils import mkdir_if_missing
from ..dataset import ImageDataset
from SoccerNet.Downloader import SoccerNetDownloader


class Soccernetv3(ImageDataset):
    """Soccernet-v3 Dataset.
    """
    dataset_dir = 'soccernetv3'
    dataset_url = None

    def __init__(self, root='', soccernetv3_training_subset=1.0, **kwargs):
        assert 1.0 >= soccernetv3_training_subset > 0.0

        self.root = osp.abspath(osp.expanduser(root))
        self.dataset_dir = osp.join(self.root, self.dataset_dir)
        # self.download_dataset(self.dataset_dir, self.dataset_url)

        self.train_dir = osp.join(self.dataset_dir, 'train')
        self.query_dir = osp.join(self.dataset_dir, 'valid/query')
        self.gallery_dir = osp.join(self.dataset_dir, 'valid/gallery')

        required_files = [
            self.dataset_dir, self.train_dir, self.query_dir, self.gallery_dir
        ]

        self.check_before_run(required_files)

        train, _, _ = self.process_dir(self.train_dir, {}, relabel=True, soccernetv3_training_subset=soccernetv3_training_subset)

        query, pid2label, ids_counter = self.process_dir(self.query_dir, {}, 0)
        gallery, pid2label, ids_counter = self.process_dir(self.gallery_dir, pid2label, ids_counter)

        super(Soccernetv3, self).__init__(train, query, gallery, **kwargs)

    def process_dir(self, main_path, pid2label, ids_counter=0, relabel=False, soccernetv3_training_subset=1.):
        data = []
        img_paths = glob.glob(osp.join(main_path, '*/*/*/*/*.png'))
        # sort images list such that each sample position in the list match its filename index
        img_paths.sort(key=lambda img_path: self.get_bbox_index(img_path))

        # if soccernetv3_training_subset is set, use samples from action '0' to action 'end_action'
        action_num = self.extract_sample_info(os.path.basename(img_paths[-1]))["action_idx"] + 1
        end_action = action_num * soccernetv3_training_subset

        for img_path in img_paths:
            filename = os.path.basename(img_path)
            info = self.extract_sample_info(filename)
            pid = info["person_uid"]
            action_idx = info["action_idx"]
            if action_idx >= end_action:
                break
            if relabel:
                if pid not in pid2label:
                    pid2label[pid] = ids_counter
                    ids_counter += 1
                pid = pid2label[pid]
            data.append((img_path, pid, action_idx))

        return data, pid2label, ids_counter

    def download_dataset(self, dataset_dir, dataset_url):
        if osp.exists(dataset_dir):
            return

        print('Creating directory "{}"'.format(dataset_dir))
        mkdir_if_missing(dataset_dir)

        print(
            'Downloading {} dataset to "{}"'.format(
                self.__class__.__name__, dataset_dir
            )
        )
        mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory=dataset_dir)
        mySoccerNetDownloader.password = "SoccerNet_Reviewers_SDATA"
        mySoccerNetDownloader.downloadDataTask(task="reid", split=["train", "valid", "test", "challenge"])

        # TODO unzip train.zip, valid.zip, test.zip, challenge.zip

        print('{} dataset is ready'.format(self.__class__.__name__))

    @staticmethod
    def extract_sample_info(filename):
        info = {}
        splits = filename.split(".")[0].split("-")
        if len(splits) == 8:
            info["bbox_idx"] = int(splits[0])
            info["action_idx"] = int(splits[1])
            info["person_uid"] = splits[2]
            info["frame_idx"] = int(splits[3])
            info["clazz"] = splits[4]
            info["id"] = splits[5]
            info["UAI"] = splits[6]
            shape = splits[7].split("x")
            info["shape"] = (int(shape[0]), int(shape[1]))
        elif len(splits) == 3:
            info["bbox_idx"] = int(splits[0])
            info["action_idx"] = int(splits[1])
            shape = splits[2].split("x")
            info["shape"] = (int(shape[0]), int(shape[1]))
        else:
            raise ValueError("Wrong sample filename format '{}'".format(filename))
        return info

    @staticmethod
    def get_bbox_index(filepath):
        return int(os.path.basename(filepath).split("-")[0])


class Soccernetv3Test(Soccernetv3):

    def __init__(self, root='', **kwargs):
        self.root = osp.abspath(osp.expanduser(root))
        self.dataset_dir = osp.join(self.root, self.dataset_dir)
        self.download_dataset(self.dataset_dir, self.dataset_url)

        self.query_dir = osp.join(self.dataset_dir, 'test/query')
        self.gallery_dir = osp.join(self.dataset_dir, 'test/gallery')

        required_files = [
            self.dataset_dir, self.query_dir, self.gallery_dir
        ]

        self.check_before_run(required_files)

        train = []
        query, pid2label, ids_counter = self.process_dir(self.query_dir, {}, 0)
        gallery, _, _ = self.process_dir(self.gallery_dir, pid2label, ids_counter)

        super(Soccernetv3, self).__init__(train, query, gallery, **kwargs)


class Soccernetv3Challenge(Soccernetv3):
    hidden_labels = True

    def __init__(self, root='', **kwargs):
        self.root = osp.abspath(osp.expanduser(root))
        self.dataset_dir = osp.join(self.root, self.dataset_dir)
        self.download_dataset(self.dataset_dir, self.dataset_url)

        self.query_dir = osp.join(self.dataset_dir, 'challenge/query')
        self.gallery_dir = osp.join(self.dataset_dir, 'challenge/gallery')

        required_files = [
            self.dataset_dir, self.query_dir, self.gallery_dir
        ]

        self.check_before_run(required_files)

        train = []
        query, pid2label, ids_counter = self.process_dir(self.query_dir, {}, 0)
        gallery, _, _ = self.process_dir(self.gallery_dir, pid2label, ids_counter)

        super(Soccernetv3, self).__init__(train, query, gallery, **kwargs)

    def process_dir(self, main_path, pid2label, ids_counter=0, relabel=False, soccernetv3_training_subset=1.):
        data = []
        img_paths = glob.glob(osp.join(main_path, '*.png'))
        # sort images list such that each sample position in the list match its filename index
        img_paths.sort(key=lambda img_path: self.get_bbox_index(img_path))

        for img_path in img_paths:
            filename = os.path.basename(img_path)
            info = self.extract_sample_info(filename)
            data.append((img_path, (info["bbox_idx"]), info["action_idx"]))

        return data, pid2label, ids_counter
