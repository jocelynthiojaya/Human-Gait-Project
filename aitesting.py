import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import csv
videos_data = pd.read_csv("csvoutput/jocelyn.csv")
videos_data.to_numpy()

list = []
x = videos_data['angles']

y = videos_data['gender']

for i in x:
    output = eval(i)
    list.append(output)
    
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(list, y, test_size = 0.20)
from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)