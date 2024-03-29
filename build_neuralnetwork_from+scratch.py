# -*- coding: utf-8 -*-
"""BUILD_NEURALNETWORK_FROM+SCRATCH

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EvVL3kL-AeA_iMvuSmRvvP57VenuXaHd
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""Loading the dataset"""

df_original = pd.read_csv('/content/drive/MyDrive/Diabetes/diabetes2-modified.csv')
df_original.head()

cols = df_original.columns.tolist()

from sklearn.feature_selection import mutual_info_classif
feature_df =df_original [['BMI','DiabetesPedigreeFunction']]
class_labels =df_original['Outcome']

feature_df=np.array(feature_df)
class_labels =np.array(class_labels)

"""Plotting"""

plt.plot(df_original,label ='Inline label')
plt.legend(['BMI','DiabetesPedigreeFunction','Outcome'])

z= np.zeros((20,2))
for i in range(20):
  z[i,class_labels[i] ] = 1

feature_df.shape

"""Adding Weights and Bias"""

w1 =np.random.randn(3,2)
b1=np.random.randn(3)
w2=np.random.randn(3,2)
b2 = np.random.randn(2)

w1

b1

w2

b2

feature_df.dot(w1.T)

"""Feed Forward Network"""

def farward_prop(feature_df,w1,ba,w2,b2):
  #first layer
  M =1/(1+np.exp(-(feature_df.dot(w1.T)+b1)))
  #2nd layer
  A = M.dot(w2) +b2
  expA = np.exp(A)
  Y = expA /expA.sum(axis = 1, keepdims = True)
  return Y,M

farward_prop(feature_df,w1,b1,w2,b2)

"""BACK PROPAGATION"""

#return gardient decent for weight2
def diff_w2(H,z,Y):
  return H.T.dot(z-Y)

#return gradient for weights
def diff_w1(feature_df,H,z,output,w2):
  dZ=(z-output).dot(w2.T)*H*(1-H)
  return feature_df.T.dot(dZ)

# return to deactivate the bias
def diff_b2(z,Y):
  return (z-Y).sum(axis = 0)
def diff_b1(z,Y,w2,H):
  return ((z-Y).dot(w2.T) * H *(1-H)).sum(axis =0)

learning_rate = 1e-3
for epoch in range(5000):
  output,hidden = farward_prop(feature_df,w1,b1,w2,b2)
  w2 += learning_rate * diff_w2(hidden,z,output)
  b2 += learning_rate * diff_b2(z,output)
  w1 +=learning_rate * diff_w1(feature_df,hidden,z,output,w2).T
  b1 +=learning_rate * diff_b1(z,output,w2,hidden)

"""Prediction"""

X_test =np.array([45.8,0.551])

hidden_output =1 /(1+np.exp(X_test.dot(w1.T)- b1))
Outer_layer_output =hidden_output.dot(w2)+ b2
expA = np.exp(Outer_layer_output)
Y = expA /expA.sum()
print("Accrracy testing >>>>> {} ".format(Y[0]))