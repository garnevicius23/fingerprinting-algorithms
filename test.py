import sklearn as sk
from sklearn import svm
import pandas as pd
import os

learn_data = pd.read_csv('my_data/data_learn.csv', sep=',', header=0)
#x_data = learn_data.iloc[:,39]
x_data = learn_data.drop('id',axis=1)
y_data = learn_data['id']

s = svm.LinearSVC(random_state=0, tol=1e-5)
var =(0,1)
var1 = [(1,1),(2,2)]
s.fit(x_data, y_data)