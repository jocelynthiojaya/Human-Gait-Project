import pandas as pd
import csv
import os
import numpy as np

directory = os.fsencode("csvoutput")

final_list = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
 
    single_video = []
    all_angles = []

    if filename.endswith(".csv"):

        # Load csv into dataframe
        df = pd.read_csv('csvoutput/' + filename)

        # Determine the gender
        gender = df.iloc[0][6]

        # Load dataframe with the wanted headers
        df_angles = df[["r_hip_ang", "r_knee_ang", "r_ankle_ang", "r_elbow_ang", "r_shoulder_ang"]]

        # Generate 1 dim list for angles
        all_angles = df_angles.values.flatten()
        all_angles = all_angles[:100].tolist()

        # Generate min angles
        min_r_hip_ang = df_angles["r_hip_ang"].min()
        min_r_knee_ang = df_angles["r_knee_ang"].min()
        min_r_ankle_ang = df_angles["r_ankle_ang"].min()
        min_r_elbow_ang = df_angles["r_elbow_ang"].min()
        min_r_shoulder_ang = df_angles["r_shoulder_ang"].min()

        # Generate max angles
        max_r_hip_ang = df_angles["r_hip_ang"].max()
        max_r_knee_ang = df_angles["r_knee_ang"].max()
        max_r_ankle_ang = df_angles["r_ankle_ang"].max()
        max_r_elbow_ang = df_angles["r_elbow_ang"].max()
        max_r_shoulder_ang = df_angles["r_shoulder_ang"].max()

        # Creating list for a single video
        single_video.append(all_angles)
        single_video.append(gender)
        single_video.append(filename)

        single_video.append(min_r_hip_ang)
        single_video.append(min_r_knee_ang)
        single_video.append(min_r_ankle_ang)
        single_video.append(min_r_elbow_ang)
        single_video.append(min_r_shoulder_ang)
        
        single_video.append(max_r_hip_ang)
        single_video.append(max_r_knee_ang)
        single_video.append(max_r_ankle_ang)
        single_video.append(max_r_elbow_ang)
        single_video.append(max_r_shoulder_ang)

        # Put everything into the final csv
        final_list.append(single_video)

# Make header for final csv
header = ['angles', 'gender', 'filename', 
        'min_r_hip_ang', 'min_r_knee_ang', 'min_r_ankle_ang', 'min_r_elbow_ang', 'min_r_shoulder_ang'
        'max_r_hip_ang', 'max_r_knee_ang', 'max_r_ankle_ang', 'max_r_elbow_ang', 'max_r_shoulder_ang']

with open('test3.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(final_list)
        