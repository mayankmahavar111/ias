# -*- coding: utf-8 -*-
import numpy as np

puredata=np.loadtxt('data.csv',delimiter=',')
X=puredata[:,:30]
Y=puredata[:,30]

print len(Y)

def cost(x, y, theta):
    m = y.size  # number of training examples
    predicted = np.dot(x, theta)
    sqErr = (predicted - y)
    J = ((1.0) / (2 * m)) * np.dot(sqErr.T, sqErr)
    return J

def gradient_descent(x, y, theta, alpha, iterations):
    m = y.size

    theta_n = theta.size

    J_theta_log = np.zeros(shape=(iterations + 1, 1))

    J_theta_log[0, 0] = cost(x, y, theta)

    for i in range(iterations):


        # split equation in to several parts
        predicted = x.dot(theta)

        for thetas in range(theta_n):
            tmp = x[:, thetas]
            tmp.shape = (m, 1)
            err = (predicted - y) * tmp
            theta[thetas][0] = theta[thetas][0] - alpha * (1.0 / m) * err.sum()
        J_theta_log[i + 1, 0] = cost(x, y, theta)

    return theta, J_theta_log


m, n = np.shape(X)

Y.shape = (m, 1)

# Add a column of ones to X as x0=1
XX = np.ones(shape=(m, 1))
XX = np.append(XX, X, 1)

# set up initial thetas to 0
theta = np.zeros(shape=(n + 1, 1))
# define number of iterations and alpha
iterations = 5000
alpha = 0.01

# calculate theta using gradient descent
theta, J_theta_log = gradient_descent(XX, Y, theta, alpha, iterations)

test=0
tp=0
tn=0
fp=0
fn=0
while test !=1000:

    if test ==-1:
        break
    index=test
    death_rate = np.array(XX[test]).dot(theta)
    if death_rate>0.5:
        death_rate=1
    else:
        death_rate=-1
    if death_rate==Y[test]==1:
        tp+=1
    elif death_rate==Y[test]==-1:
        tn+=1
    elif death_rate==1 and Y[test]==-1:
        fn+=1
    elif death_rate==-1 and Y[test]==1:
        fp+=1
    test+=1
Accuracy=(tp+tn)/float(tp+fn+fp+tn)
Recall=tp/float(tp+fn)
Precision=tp/float(tp+fp)
print "Accuracy : " ,Accuracy
print "Recall : " ,Recall
print "Precision : ",Precision
print "F1 measure : ",2*(Recall * Precision) / (Recall + Precision)

