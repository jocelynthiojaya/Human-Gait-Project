import pandas as pd
import csv
import os

directory = os.fsencode("csvoutputfinal")

li = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
 
    df = pd.read_csv('csvoutputfinal/' + filename, index_col=None, header=0)
    li.append(df)

final_frame = pd.concat(li, axis=0, ignore_index=True)

print(final_frame)

final_frame.to_csv('femalewalk.csv', index=False)