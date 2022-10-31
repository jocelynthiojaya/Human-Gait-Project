import pandas as pd
import os
import csv

directory = os.fsencode("csvoutput")

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith(".csv"):

        fps = 30

        # Load csv into dataframe
        df = pd.read_csv('csvoutput/' + filename)
        df_angles = df[["r_hip_ang", "r_knee_ang", "r_ankle_ang", "r_elbow_ang", "r_shoulder_ang"]]
        df_frames = df[["frame"]]

        # Calculate time (frame/fps)
        df_time = df_frames.div(fps, axis=0)
        #print(df_time)

        # Calculate difference between angles
        delta_angles = df_angles.diff(axis=0)
        delta_angles = delta_angles.fillna(0)
        #print(delta_angles)

        # Calculate velocity (delta theta / time)
        velocity = delta_angles.div(df_time.frame, axis=0)
        #print(velocity)

        # Calculate acceleration
        acceleration = velocity.div(df_time.frame, axis=0)
        #print(acceleration)

        # Append dataframes
        df[["r_hip_vel", "r_knee_vel", "r_ankle_vel", "r_elbow_vel", "r_shoulder_vel"]] = velocity
        df[["r_hip_accel", "r_knee_accel", "r_ankle_accel", "r_elbow_accel", "r_shoulder_accel"]] = acceleration
        #print(df)

        # Write to csv
        df.to_csv('csvoutputfinal/' + filename, index=False)