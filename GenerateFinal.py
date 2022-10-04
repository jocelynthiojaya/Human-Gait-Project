import pandas as pd
import csv
import os

directory = os.fsencode("csvoutput")

final_list = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
 
    single_video = []
    all_angles = []
    #single_frame = []

    if filename.endswith(".csv"):

        df = pd.read_csv('csvoutput/' + filename)
        #print(df)

        gender = df.iloc[0][6]
        #print(gender)

        # for row in df.index:
        #     for col in range(5):
        #         single_frame.append(df.iloc[row][col+1])
        #         #print(angles_list)
        #     all_frames.append(single_frame)
        #     single_frame = []
        #print(all_frames)
        df_angles = df[["r_hip_ang", "r_knee_ang", "r_ankle_ang", "r_elbow_ang", "r_shoulder_ang"]]
        all_angles = df_angles.values.tolist()

        single_video.append(all_angles)
        single_video.append(gender)
        single_video.append(filename)
        # single video is one row correct

        final_list.append(single_video)

header = ['angles','gender']
with open('test2.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(final_list)
        

#print(final_list)

    