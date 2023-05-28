# Guidelines for the SoccerNet Re-Identification Challenge

The 2nd [SoccerNet Person Re-Identification Challenge]() will be held from February to June 2023!
Subscribe (watch) the repo to receive the latest info regarding timeline and prizes!


SoccerNet-v3 ReID is a large-scale dataset build upon SoccerNet that benchmarks the task of player re-identification across multiple camera views from broadcast soccer videos. 
SoccerNet-v3 is composed of 300k manual annotations, span 500 complete soccer games from six main European leagues, covering three seasons from 2014 to 2017 and a total duration of 764 hours.

We propose the SoccerNet-v3 ReID challenge to encourage the development of state-of-the-art ReID algorithm for sport player retrieval in broadcast videos.

We provide an [evaluation server](https://eval.ai/web/challenges/challenge-page/1548/) for anyone competing in the SoccerNet-v3 ReID challenge. 
This evaluation server handles predictions for the open **test** set and the segregated **challenge** set.

Winners will be announced during the CVSports workshop at CVPR in June 2023. 
Prizes 💲💲💲 include $500 cash award, sponsored by [Synergy Sports](https://synergysports.com/), a [SportRadar](https://www.sportradar.com/) division.


## Who can participate / How to participate?

 - Any individual can participate in the challenge, except the organizers.
 - The participants are recommended to form a team to participate.
 - Each team can have one or more members. 
 - An individual/team can compete on both task.
 - An individual associated with multiple teams (for a given task) or a team with multiple accounts will be disqualified.
 - To solve the ReID task, a participant can only use player image crops and labels provided in the SoccerNet-v3 ReID dataset, which means using external information from other versions of the SoccerNet-v3 dataset is forbidden. Participants can therefore only rely on player appearance to solve the task.
 - Any information within image crops or sample labels can be used to solve the task: global body appearance, facial recognition, OCR for jersey numbers, ...
 - Participants can use any **public** dataset to pretrain their model. Any public dataset or codebase used for the challenge must be mentioned in the final report.
 - Participants are allowed to train their final model on all provided data (train + valid + test sets) before evaluating on the challenge set.
 - If you have any doubts regarding these rules, please contact the challenge administrators.


## How to win / What is the prize?

 - The winner will the individual/team who reaches the highest **mAP** performance on the **challenge** set.
 - The deadline to submit your results is May 30th at 11.59 pm  Pacific Time.
 - The teams that perform best in each task will be granted $500 from our sponsor [Synergy Sports](https://synergysports.com/), a [SportRadar](https://www.sportradar.com/) division.
 - In order to be eligible for the prize, we require the individual/team to provide a short report describing the details of the methodology (CVPR format, max 3 pages)


## Important dates

Note that these dates are tentative and subject to change if necessary.

 - **February 6:** Open evaluation server on the (Open) Test set.
 - **February 6:** Open evaluation server on the (Segregated) Challenge set.
 - **May 30:** Close evaluation server.
 - **June 6:** Deadline for submitting the report.
 - **June TBD:** A full-day workshop at CVPR 2022.


## Contact

For any further doubt or concern, please raise a GitHub issue in this repository, or contact us directly on [Discord](https://discord.gg/SM8uHj9mkP).
