import whois
import datetime



f=open('top-1m.csv','r')
dataset=f.readlines()[1:]
dic={'name':0,'dnssec' : 0, 'city' : 0, 'zipcode':0,'country':0,'state':0,'referral_url':0,'address':0,'org':0}

for i in range(len(dataset)):
    print i
    if i > 100:
        break
    line=dataset[i]
    line = line.split(',')[1]
    line = line.split('\n')[0]
    #line=line.split(':/')[1]
    #line=line.split('/')[1]
    try:
        x=whois.whois(line)
        for j in dic:
            if x.j == None :
                dic[j]+=1
    except Exception as e:
        print e
        print line

for j in dic:
    print j,':',dic[j]
