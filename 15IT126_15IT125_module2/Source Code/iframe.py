f=open('data.html','r')
data=f.readlines()
f.close()

for line in data:
    if 'iframe' in line and 'border-width:' in line:
        temp=line.split('border-width:')[1]
        temp=temp.split(';')[0]
        print temp , '0' in temp