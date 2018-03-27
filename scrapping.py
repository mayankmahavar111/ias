f=open('data.html','r')
data=f.readlines()
f.close()

dataset=[]

for line in data:
    if '://' in line :
        line=line.split('://')
        line=line[1:]
        temp=[]
        for x in line:
            temp.append(x.split('"')[0])
        line=temp
        for x in line:
            dataset.append(x)
#print len(dataset)
count=0
for x in dataset:
    if 'google' in x:
        count+=1
#print count

