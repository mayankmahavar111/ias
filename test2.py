import whois


f=open('top-1m.csv','r')
dataset=f.readlines()
count=0

for i in range(len(dataset)):
    if i>100:
        break
    line=dataset[i]
    line = line.split(',')[1]
    line = line.split('\n')[0]
    x=whois.whois(line)
    if x.updated_date == None:
        count+=1

print count