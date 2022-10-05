import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import csv
from ast import literal_eval
videos_data = pd.read_csv("csvoutput/vincent_result.csv")
list = []
x = videos_data.drop(['gender','filename'], axis = 1)

y = videos_data['gender']

for i in x['angles'].values:
    output = literal_eval(i)
    list.append(output)
    
x['angles'] = list
print(x.head())
X_train, X_test, y_train, y_test = train_test_split(list, y, test_size = 0.20)
svclassifier = SVC(kernel='rbf')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)

from sklearn import metrics


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# from sklearn.metrics import classification_report, confusion_matrix
# print(confusion_matrix(y_test,y_pred))
# print(classification_report(y_test,y_pred))