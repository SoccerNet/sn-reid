# SoccerNet Re-Identification
Welcome to the Development Kit for the SoccerNet Re-Identification Task and Challenge.
This kit is meant as a help to get started working with the SoccerNet data and the proposed task.
In this task, participants will have to re-identify soccer players across multiple camera viewpoints.
More information about the dataset can be found on our [official website](https://soccer-net.org/).
In this repository, you will find all the instructions and codebase for participating in this challenge and get a chance to win the 1000$ prize money!
The winner of the competition will be announced in June 2022.

SoccerNet Re-Identification (ReID) is part of the SoccerNet-v3 dataset, which is an extension of SoccerNet-v2 with new and challenging tasks including 
action spotting, camera shot segmentation with boundary detection, replay grounding, calibration, multi-view player re-identification and multi-player tracking.

<a href="">
<p align="center"><img src="images/Thumbnail.png" width="720"></p>
</a>

[comment]: <> (<p align="center"><img src="images/GraphicalAbstract-SoccerNet-V2-1.png" width="640"></p>)


The participation deadline is fixed at the 30th of May 2022.
The official rules and guidelines are available on [ChallengeRules.md](ChallengeRules.md).

<p align="center"><img src="images/multiview_links.png" width="640"></p>

## Challenge description
The SoccerNet Re-Identification (ReID) dataset is composed of 340.993 players thumbnails extracted from image frames of broadcast videos from 400 soccer games within 6 major leagues.
The goal of the challenge is to re-identify soccer players across multiple camera viewpoints depicting the same action during the game.

Compared to traditional street surveillance type re-identification dataset, the SoccerNet-v3 ReID dataset is particularly \ 
challenging because soccer players from the same team have very similar appearance, which makes it hard to tell them apart.


## Instructions
This repo is a fork of the [Torchreid](https://github.com/KaiyangZhou/deep-person-reid) framework for person re-identification.
Make sure to have a look at the original [Torchreid Readme](TORCHREID_README.rst) and the official [Torchreid documentation](https://kaiyangzhou.github.io/deep-person-reid/.) for detailed how-to instructions.

### How to install Torchreid
For installation guidelines, please follow the instructions in the original [Torchreid Readme](TORCHREID_README.rst).

### How to train and test a baseline model
We provide a basic script in [benchmarks/baseline](benchmarks/baseline) for training a baseline model on the Soccernet-v3 training set, evaluate rank-1 and mAP performance on the Soccernet-v3 \
validation and test set, and finally export ranking results on the Soccernet-v3 challenge set for external evaluation.

To train the baseline model, run:

<code>python benchmarks/baseline/main.py --config-file configs/baseline_config.yaml</code>

Running this script will automatically download the dataset in the folder specified by the _data.root_ config.

Have a look at the YAML configuration file [baseline_config.yaml](benchmarks/baseline/configs/baseline_config.yaml) and related default configuration [default_config.py](benchmarks/baseline/default_config.py) for more information about the available options.

### How to manually download the dataset
A [SoccerNet pip package](https://pypi.org/project/SoccerNet/) is available to easily download the data and the annotations. 

To install the pip package simply run:

<code>pip install SoccerNet</code>

Then use the API to download the data of interest:

```
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="/path/to/SoccerNet")
mySoccerNetDownloader.downloadDataTask(task="reid", split=["train", "valid", "test", "challenge"])
```
### How to export your ranking results for the challenge set
Enable the `test.export_ranking_results` config in [default_config.py](benchmarks/baseline/default_config.py) or [baseline_config.yaml](benchmarks/baseline/configs/baseline_config.yaml) 
to export all ranking results for each target dataset. 
Ranking results will be exported to a JSON file `ranking_results_***.json` in the directory specified by the `data.save_dir` config.

To export ranking results for the SoccerNet ReID challenge set, make sure to add 'soccernetv3_challenge' to the list of target datasets in the `data.targets` config.


### How to submit your ranking results to participate in the challenge
The resulting JSON file should be submitted on the online evaluation platform.
Further information will be provided soon.


## Future improvements
This repository will be actively maintained during the course of the challenge, make sure to subscribe and come back frequently to get the latest updates!
Here are some of the things we plan to add or improve:
- An eval.py script to compute performance of exported ranking result in JSON format.
- A more accurate description of the dataset structure and file naming convention.
- Some stats about the dataset size.
- Faster ranking script in rank.py to assess model performance.
- ...

Feel free to suggest any changes.


## Our other Challenges
Check out our other challenges related to SoccerNet:
- [Action Spotting](https://github.com/SoccerNet/sn-spotting)
- [Replay Grounding](https://github.com/SoccerNet/sn-grounding)
- [Calibration](https://github.com/SoccerNet/sn-calibration)
- [Re-Identification](https://github.com/SoccerNet/sn-reid)
- [Tracking](https://github.com/SoccerNet/sn-tracking)


## Citation
For further information check out the paper and supplementary material:
https://openaccess.thecvf.com/content/CVPR2021W/CVSports/papers/Deliege_SoccerNet-v2_A_Dataset_and_Benchmarks_for_Holistic_Understanding_of_Broadcast_CVPRW_2021_paper.pdf

Please cite our work if you use our dataset:
```bibtex
@InProceedings{Deliège2020SoccerNetv2,
      title={SoccerNet-v2 : A Dataset and Benchmarks for Holistic Understanding of Broadcast Soccer Videos}, 
      author={Adrien Deliège and Anthony Cioppa and Silvio Giancola and Meisam J. Seikavandi and Jacob V. Dueholm and Kamal Nasrollahi and Bernard Ghanem and Thomas B. Moeslund and Marc Van Droogenbroeck},
      year={2021},
      booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
      month = {June},
}
```


## Useful links
- [Soccernet official website](https://soccer-net.org/)
- [ACAD Research](https://www.youtube.com/channel/UCYkYA7OwnM07Cx78iZ6RHig)
- [Torchreid](https://github.com/KaiyangZhou/deep-person-reid)


## Questions and Remarks
If you have any question or remark regarding the challenge and related materials, please raise a GitHub issue in this repository, or contact us directly on [Discord](https://discord.gg/SM8uHj9mkP).


## Sponsorship
This challenge is officially sponsored by [Synergy Sports](https://synergysports.com/), a division of [Sportradar](https://www.sportradar.com/).

