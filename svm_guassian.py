from sklearn import datasets
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

puredata=np.loadtxt('data.csv',delimiter=',')
X=puredata[:,:30]
Y=[]

for x in puredata:
    Y.append(x[30])

clf=svm.SVC()
clf.fit(X,Y)

pred=clf.predict(X)
cm=confusion_matrix(Y,pred)

print cm

tp=cm[0][0]
fp=cm[0][1]
fn=cm[1][0]
tn=cm[1][1]

accuracy=round(float(tp+tn)/float(tp+tn+fp+fn),4)

print accuracy