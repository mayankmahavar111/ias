import csv
from collections import defaultdict
import math

mylist=[]
classlist=[]
test= defaultdict(list)
classes= defaultdict(list)

def findprob(x,mean,stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

def calculateprob(mean,variance,key ,test ,j):

    for i in range(len(mean["class"])):
        prob = 1
        if mean["class"][i] == key:
            for x in mylist :
                if x !="class":
                    prob =prob * findprob(float(test[x][j]),mean[x][i],variance[x][i])
            finalprob= prob
    return finalprob





def findvariance(dataset , key ,temp, mean):
    global mylist
    for x in mylist:
        if x != 'class':
            count = 0
            sum = 0
            for i in range(len(mean["class"])):
                if mean["class"][i] == key :
                    mea = mean[x][i]
                    break
            for i in range(len(dataset[x])):
                if dataset["class"][i] == key:
                    sum = sum + pow(mea-float(dataset[x][i]),2)
                    count = count + 1
            variance = sum/count
            variance = math.sqrt(variance)
            temp[x].append(variance)
    temp["class"].append(key)
    return temp

def findmean(dataset,key , temp):
    global mylist
    for x in mylist :
        if x !='class':
            count = 0
            sum = 0
            for i in range(len(dataset[x])):
                if dataset["class"][i] == key :
                    sum  = sum + float(dataset[x][i])
                    count = count +1
            mean = sum/count
            temp[x].append(mean)
    temp["class"].append(key)
    return temp

"""
def classdataset(dataset):
    global mylist,classes,classlist
    temp =defaultdict(list)
    classlist= list(set(dataset["class"]))
    print classlist , len(classlist)
    for x in classlist:
        for i in range(len(dataset["class"])):
            if dataset["class"][i] == x :
                for j in mylist :
                    if j != "class":
                        temp[x].append(dataset[j][i])
    print len(temp),temp['Iris-setosa']
    return temp
"""
def split(dataset,ratio):
    global mylist,test
    temp = defaultdict(list)
    number= len(dataset["class"]) * ratio
    number= int(number)

    for x in mylist:
        i=0
        for j in dataset[x]:
            if i<number:
                temp[x].append(j)
            else:
                test[x].append(j)
            i=i+1

    return temp

def loadcsv(file):
    global mylist
    columns = defaultdict(list)  # each value in each column is appended to a list

    with open(file) as f:
        reader = csv.DictReader(f)# read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():
                mylist.append(k.lower())# go over each column name and value
                columns[k.lower()].append(v)
    mylist= list(set(mylist))
    #print len(columns),len(mylist)
    return columns

def main():
    global mylist,test
    dataset=loadcsv("SPECTF_New.csv")
    len(mylist)
    dataset=split(dataset,0.67)
    classlist = list(set(dataset["class"]))
    #print len(classlist),classlist
    mean =  defaultdict(list)
    for x in classlist :
        mean = findmean(dataset,x ,mean)
    #print len(mean)
    variance = defaultdict(list)
    for x in classlist:
        variance = findvariance(dataset,x,variance,mean)

    result = defaultdict(list)
    resultlist = []
    for i in range(len(test["class"])):
        for x in mylist :
            temp = classlist[0]
            maxprob=0
            for x in classlist:
                tempprob = calculateprob(mean,variance,x,test ,i)
                if tempprob > maxprob :
                    maxprob =tempprob
                    temp =x
        test["Predicted"].append(temp)
    mylist.append("Predicted")
    count = 0
    total = 0
    for i in range(len(test["class"])):
        for x in mylist :
            #print test[x][i],
            if x == "class" :
                clas= test[x][i]
            if  x == "Predicted" :
                pred= test[x][i]
        #rint "\n"
        if clas == pred :
            count = count +1
        total = total +1
    print "accuracy is ",
    print float(count)/float(total)
main()