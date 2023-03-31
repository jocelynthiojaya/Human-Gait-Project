import pandas as pd
import os
import csv

folder = "foldername"
nametag = "tag"
directory = os.fsencode(folder + "/" + nametag + "_csvoutput/")

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith(".csv"):

        fps = 30

        # Load csv into dataframe
        df = pd.read_csv(folder + "/" + nametag + "_csvoutput/" + filename)
        df_angles = df[["r_hip_ang", "r_knee_ang", "r_ankle_ang", "r_elbow_ang", "r_shoulder_ang"]]
        df_frames = df[["frame"]]

        # Calculate time (frame/fps)
        df_time = df_frames.div(fps, axis=0)

        # Calculate difference between angles
        delta_angles = df_angles.diff(axis=0)
        delta_angles = delta_angles.fillna(0)

        # Calculate velocity (delta theta / time)
        velocity = delta_angles.div(df_time.frame, axis=0)

        # Calculate acceleration
        acceleration = velocity.div(df_time.frame, axis=0)

        # Append dataframes
        df[["r_hip_vel", "r_knee_vel", "r_ankle_vel", "r_elbow_vel", "r_shoulder_vel"]] = velocity
        df[["r_hip_accel", "r_knee_accel", "r_ankle_accel", "r_elbow_accel", "r_shoulder_accel"]] = acceleration

        # This shifts for each video ya 
        # Duplicate columns
        df[["r_hip_ang_2", "r_knee_ang_2", "r_ankle_ang_2", "r_elbow_ang_2", "r_shoulder_ang_2"]] = df[["r_hip_ang", "r_knee_ang", "r_ankle_ang", "r_elbow_ang", "r_shoulder_ang"]]
        df[["r_hip_ang_3", "r_knee_ang_3", "r_ankle_ang_3", "r_elbow_ang_3", "r_shoulder_ang_3"]] = df[["r_hip_ang", "r_knee_ang", "r_ankle_ang", "r_elbow_ang", "r_shoulder_ang"]]

        df[["r_hip_vel_2", "r_knee_vel_2", "r_ankle_vel_2", "r_elbow_vel_2", "r_shoulder_vel_2"]] = df[["r_hip_vel", "r_knee_vel", "r_ankle_vel", "r_elbow_vel", "r_shoulder_vel"]]
        df[["r_hip_vel_3", "r_knee_vel_3", "r_ankle_vel_3", "r_elbow_vel_3", "r_shoulder_vel_3"]] = df[["r_hip_vel", "r_knee_vel", "r_ankle_vel", "r_elbow_vel", "r_shoulder_vel"]]

        df[["r_hip_accel_2", "r_knee_accel_2", "r_ankle_accel_2", "r_elbow_accel_2", "r_shoulder_accel_2"]] =  df[["r_hip_accel", "r_knee_accel", "r_ankle_accel", "r_elbow_accel", "r_shoulder_accel"]]
        df[["r_hip_accel_3", "r_knee_accel_3", "r_ankle_accel_3", "r_elbow_accel_3", "r_shoulder_accel_3"]] =  df[["r_hip_accel", "r_knee_accel", "r_ankle_accel", "r_elbow_accel", "r_shoulder_accel"]]

        # Shift data
        df[["r_hip_ang_2", "r_knee_ang_2", "r_ankle_ang_2", "r_elbow_ang_2", "r_shoulder_ang_2"]] = df[["r_hip_ang_2", "r_knee_ang_2", "r_ankle_ang_2", "r_elbow_ang_2", "r_shoulder_ang_2"]].shift(periods=3)
        df[["r_hip_ang_3", "r_knee_ang_3", "r_ankle_ang_3", "r_elbow_ang_3", "r_shoulder_ang_3"]] = df[["r_hip_ang_3", "r_knee_ang_3", "r_ankle_ang_3", "r_elbow_ang_3", "r_shoulder_ang_3"]].shift(periods=6)

        df[["r_hip_vel_2", "r_knee_vel_2", "r_ankle_vel_2", "r_elbow_vel_2", "r_shoulder_vel_2"]] = df[["r_hip_vel_2", "r_knee_vel_2", "r_ankle_vel_2", "r_elbow_vel_2", "r_shoulder_vel_2"]].shift(periods=3)
        df[["r_hip_vel_3", "r_knee_vel_3", "r_ankle_vel_3", "r_elbow_vel_3", "r_shoulder_vel_3"]] = df[["r_hip_vel_3", "r_knee_vel_3", "r_ankle_vel_3", "r_elbow_vel_3", "r_shoulder_vel_3"]].shift(periods=6)

        df[["r_hip_accel_2", "r_knee_accel_2", "r_ankle_accel_2", "r_elbow_accel_2", "r_shoulder_accel_2"]] = df[["r_hip_accel_2", "r_knee_accel_2", "r_ankle_accel_2", "r_elbow_accel_2", "r_shoulder_accel_2"]].shift(periods=3)
        df[["r_hip_accel_3", "r_knee_accel_3", "r_ankle_accel_3", "r_elbow_accel_3", "r_shoulder_accel_3"]] = df[["r_hip_accel_3", "r_knee_accel_3", "r_ankle_accel_3", "r_elbow_accel_3", "r_shoulder_accel_3"]].shift(periods=6)
        
        # Fill null with 0
        df = df.fillna(0)

        # Write to csv
        df.to_csv(folder + "/" + nametag + "_csvoutputVA/" + filename, index=False)

print("finished")