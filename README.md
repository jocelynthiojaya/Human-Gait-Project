# Human-Gait-Project
Project studying human gait patterns by Binus University Students, Jocelyn Thiojaya and Vincentius Gabriel.

Below is a brief explanation of the purpose of each file.

**addid.py**
Used to add the "id" column to data in a csv file.

**ConcatFrames.py**
Used to concatenate all csv files within a folder, into one csv file.

**PoseModule.py**
Functions using Mediapipe's Pose Detection to draw landmarks and calculate joint angles. Credit to https://github.com/aryanvij02/PushUpCounter 

**WalkingLoop.py**
Takes a folder with .mp4 videos and generates data of joint angles, making 3 outputs:
- Videos with landmarks drawn on top
- Csv files containing angular data by calling **OutputCsv.py**
- Graph images of angular data by calling **OutputGraph.py**

**WalkingOnce.py**
Has the same usage as **WalkingLoop.py**, but only takes a single .mp4 video.

**GenerateVelocityAccel.py**
Takes a folder with csv files from the results of **WalkingLoop.py** or **WalkingOnce.py**, and generates columns for velocity, acceleration, and sequential data, outputs into a new folder.

**GnbVelocity.ipynb**
Used to train and test Gaussian Naive Bayes models.

**RandomForest.ipynb**
Used to train and test Random Forest models.

**SvmVelocity.ipynb**
Used to train and test SVM models.

**Xgboost.ipynb**
Used to train and test XGBoost models.

**NeuralKeras.ipynb**
Used to train and test Neural Network models.

**TestingModels.ipynb**
Used to do further testing on exported models.
