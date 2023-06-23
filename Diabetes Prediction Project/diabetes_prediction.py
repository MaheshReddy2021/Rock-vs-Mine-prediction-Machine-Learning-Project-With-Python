# -*- coding: utf-8 -*-
"""Diabetes Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_bYSmQmqe94RUZHN3PT_b-mfjBL_ovEK
"""

import numpy as np
import pandas as pd
from sklearn import svm # support vector machine classifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # StandardScaler used to standardization of the data
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import seaborn as sns
from sklearn.metrics import confusion_matrix

"""Data collection and Analysis Of The Diabetes Data"""

dataset = pd.read_csv("/content/diabetes.csv")

dataset.shape

dataset.head() # we can print the first 5 rows of the dataframe by using head()

"""0 ---> Non Diabetic

1 ---> Diabetic
"""

# getting the statistical measures of the data
dataset.describe()

dataset["Outcome"].value_counts()

dataset.groupby("Outcome").mean()

X = dataset.drop(columns="Outcome" , axis=1)
Y = dataset["Outcome"]

"""Finding number of null alues in the dataset"""

dataset.isnull().sum()
#below result shows that there is no null values

print(X)
print(Y)

"""Data Standardization"""

diabetes_scaler = StandardScaler()

diabetes_scaler.fit(X)

diabetes_standardized_data = diabetes_scaler.transform(X)

print(diabetes_standardized_data)

X = diabetes_standardized_data
Y = dataset["Outcome"]

print(X)
print(Y)

"""Splitting the data into Train and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify = Y ,random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Training the model with training data"""

diabetes_classifier = svm.SVC(kernel = "linear", C = 5)

# training the support vector machine classifier
diabetes_classifier.fit(X_train , Y_train)

"""Model Evaluation

Accuracy Score

accuracy score on the training data
"""

X_train_prediction = diabetes_classifier.predict(X_train)
trainiing_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print(" Accuracy score of the tarining data :" , trainiing_data_accuracy)

""" Accuracy score on the test data"""

X_test_prediction = diabetes_classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print(" Accuracy score of the test data :" , test_data_accuracy)

"""Confusion matrix"""

diabetes_confusion_matrix = confusion_matrix(Y_test, X_test_prediction)
print(diabetes_confusion_matrix)

tn,fp,fn,tp = diabetes_confusion_matrix.ravel()
print(tn,fp,fn,tp)

sns.heatmap(diabetes_confusion_matrix, annot = True)

"""Precision"""

#precision for the training data
diabetes_precision_train = precision_score(Y_train,X_train_prediction)
print("Training data precision = ", diabetes_precision_train)
# precision for the test data
diabetes_precision_test = precision_score(Y_test,X_test_prediction)
print("Test data precision = ", diabetes_precision_test)

"""Recall"""

# Recall for the training data
diabetes_recall_train = recall_score(Y_train,X_train_prediction)
print("Training data recall = ", diabetes_recall_train)
# recall for the test data
diabetes_recall_test = recall_score(Y_test,X_test_prediction)
print("Test data recall = ", diabetes_recall_test)

"""F1 score"""

# f1 score for traing data
diabetes_f1_score_train = f1_score(Y_train, X_train_prediction)
print(" f1 score on train data : " ,diabetes_f1_score_train)

# f1 score for test data
diabetes_f1_score_test = f1_score(Y_test, X_test_prediction)
print(" f1 score on test data : " ,diabetes_f1_score_test)

"""Making a Predictive system"""

input_data = (1,89,66,23,94,28.1,0.167,21)

# changeing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# replace the array as we are predicting for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


# standardize the input data

std_data = diabetes_scaler.transform(input_data_reshaped)
print(std_data)

prediction = diabetes_classifier.predict(std_data)

print(prediction)

if (prediction[0]==0):
  print("person is not diabetic")

else:
  print("person is diabetic")

