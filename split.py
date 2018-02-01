import progressbar


f=open('dataset.txt','r')
dataset=f.readlines()

f=open('train.txt','w')
t=open('test.txt','w')

bar=progressbar.ProgressBar()

for i in bar(range(len(dataset))):
    if float(i)/float(len(dataset))<0.9:
        f.write(dataset[i])
    else:
        t.write(dataset[i])
