f=open('data.html','r')
data=f.read()
f.close()

data=data.split('head')[1]
print data
