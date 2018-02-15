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
        print len(line)
        print line
        dataset.append(line)
        break
