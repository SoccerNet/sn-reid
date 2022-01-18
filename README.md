# SoccerNet - Re-Identification
Welcome to the SoccerNet Development Kit for the Re-Identification Task and Challenge. \
This kit is meant as a help to get started working with the soccernet data and the proposed task. 
More information about the dataset can be found on our [official website](https://soccer-net.org/).
In this repository, you will find all the instructions and codebase for participating to this challenge and get a chance to win the 1000$ prize money!
The winner of the competition will be announced during the CVSport workshop at CVPR 2022.

SoccerNet Action Spotting is part of the SoccerNet-v2 dataset, which is an extension of SoccerNet-v1 with new and challenging tasks including
action spotting, camera shot segmentation with boundary detection, and a novel replay grounding task.


## Challenge description
The goal of this competition is to re-identify soccer player across multiple images captured from various camera viewpoints.
In this Soccernet ReID dataset, we provide a list of xxx soccer actions, each actions being composed of multiple image frames captured at the same time from various camera viewpoints.
Explain action frame vs replay frame
The goal of the challenge is to re-identify each soccer player seen in the action frame across the different replay frame.
For that purpose, each bounding box in each action frame will be considered as a query, and bounding boxes from the corresponding replay frame will be ranked according to their distance to this query.
The dataset is divided into a training, validation, test and challenge set.
Labels for the challenge set are kept secret as participants to the challenge will be ranked according to their performance on that challenge set.
The winner of the challenge will be the participant with the highest mAP score on the challenge set. 

challenge objective: ranking action vs replay + perf metric
testing is performed within same action
Compared to traditional street surveillance type re-identification dataset, the Soccernet-v3 ReID dataset is particularly \ 
challenging because of football players from the same team have very similar appearance, which makes it hard to tell them apart.
On the other hand, each identity has a few number of samples, which render the model harder to train.
There is also a big variation in image resolution.

![alt text](projects/soccernet-v3/figures/soccernet-v3-reid-illustration-saved.pdf)


## Dataset structure

ReID samples are organized following the original Soccernet dataset structure.
The Soccernet-v3 ReID dataset is organized within a tree folder structure :
root -> set type {train, valid, test, challenge} -> championship -> season -> game -> action
Each action contains a set of samples, which are bounding boxes of players or referees cropped from the original Soccernet-v3 dataset.
Annotations are provided within the sample filename:

Naming convention:
e.g. '192245_1798_0_11_Player-team-right_a_125a000322b119fb0014.png'
<person_idx>_<action_idx>_<frame_idx>_<bbox_idx>_<class>_<ID>_<UAI>.png

1. person_idx: index from 0 to xxx, unique for each identity within an given action_idx
2. action_idx: action index, unique for each action frame and its related replay frames
3. frame_idx: frame index, 0 for action frame and >0 for replay frames
4. bbox_idx: bbox index (among other 'person' bboxes) within the given frame
5. class: bbox type/class within :
	1. "Player team left"
	2. "Player team right"
	3. "Goalkeeper team left"
	4. "Goalkeeper team right"
	5. "Main referee"
	6. "Side referee"
	7. "Staff members"
	8. "Player team unknown 1"
	9. "Player team unknown 2"
	10.  "Goalkeeper team unknown"
6. ID: link ID from soccernet-v3 annotations
7. UAI: item UAI from soccernet-v3 annotations

Important note: player identities have been annotated only within one action, which means that a player has a
different identity for each action he as been spotted in. This means that player ids are do not hold cross actions and are only valid within a given action.


## Instructions

Here we provide a basic script for training a baseline model on the Soccernet-v3 training set, test it on the Soccernet-v3 \
eval and test set and export ranking results on the Soccernet-v3 challenge set.
Basic baseline script + basic config

This repo is a fork of the [Torchreid](https://github.com/KaiyangZhou/deep-person-reid) framework for person re-identification.
Make sure to have a look at the original Torchreid README in [TORCHREID_README.rst] for detailed installation and how-to instructions.



## What has been changed from the original Torchreid codebase

- new Soccernet dataset class, 3 classes for 3 datasets
- Custom evaluation script to assess model performance on Soccernet
- New option to export ranking results
- camid within code is replaced with action index and in rank.y, that info is used to remove gallery samples from other actions


## Useful links
- [Soccernet website](https://soccer-net.org/)
- [ACAD Research](https://www.youtube.com/channel/UCYkYA7OwnM07Cx78iZ6RHig)
- [Torchreid](https://github.com/KaiyangZhou/deep-person-reid)


## Our other Challenges
Check out our other challenges related to SoccerNet!
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

## Questions and Remarks
If you have any question or remark regarding the challenge and related materials, feel free to open a Github issue.

## Keywords
Person re-identification, re-id, ReID, Soccernet, computer vision, sport, AI, deep learning, Pytorch, Torchreid, CVPR, challenge

## Sponsorship
This challenge is officially sponsored by [Synergy Sports](https://synergysports.com/), a division of [Sportradar](https://www.sportradar.com/)


[comment]: <> (TODO)
[comment]: <> samples from action frame with no match have been put in gallery
[comment]: <> action with no human bbox removed
[comment]: <> Frames/actions with no human bbox
[comment]: <> Annotation errors: multiples person with same link ID
[comment]: <> Actions with no links, i.e. with no bbox that could be used as query
[comment]: <> 
[comment]: <> 
[comment]: <> 
[comment]: <> 
[comment]: <> 
[comment]: <> 
[comment]: <> 
