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

        # Load csv into dataframe
        df = pd.read_csv('csvoutput/' + filename)

        # Determine the gender
        gender = df.iloc[0][6]

        df_angles = df[["r_hip_ang", "r_knee_ang", "r_ankle_ang", "r_elbow_ang", "r_shoulder_ang"]]
        all_angles = df_angles.values.flatten()
        all_angles = all_angles[:100].tolist()

        single_video.append(all_angles)
        single_video.append(gender)
        single_video.append(filename)

        final_list.append(single_video)

header = ['angles', 'gender', 'filename']
with open('test2.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(final_list)
        

#print(final_list)

    