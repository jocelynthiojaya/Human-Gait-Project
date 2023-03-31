import pandas as pd
import csv
import os

folder = "temp"
directory = os.fsencode(folder)

li = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
 
    df = pd.read_csv(folder + '/' + filename, index_col=None, header=0)
    li.append(df)

final_frame = pd.concat(li, axis=0, ignore_index=True)

#print(frame)

final_frame.to_csv(folder + '/walk.csv', index=False)