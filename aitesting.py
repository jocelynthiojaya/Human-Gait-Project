import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import csv

videos_data = pd.read_csv("csvoutput/test2.csv")
videos_data.to_numpy()

list = []
x = videos_data['angles']

y = videos_data['gender']

for i in x:
    output = eval(i)
    list.append(output)
    
X_train, X_test, y_train, y_test = train_test_split(list, y, test_size = 0.20)
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)

print(list[0])