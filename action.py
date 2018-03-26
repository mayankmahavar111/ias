f=open('data.html','r')
data=f.readlines()
f.close()

for line in data:
    if '<form ' in line and 'action' in line:
        test = line.split('action="')[1]
        test=test.split('"')[0]
        print (len(test))
        print (test)