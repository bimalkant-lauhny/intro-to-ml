#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel="rbf", C=10000)
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
tt = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-tt, 3), "s"

tp = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-tp, 3), "s"

print accuracy_score(pred, labels_test)
chrisN = 0
for i in range(len(pred)):
    if pred[i] == 1:
        chrisN = chrisN + 1
print "answer: ", chrisN 
#########################################################


