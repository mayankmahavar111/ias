import re

f=open('data.html','r')
data=f.readlines()
f.close()

dataset=[]

for line in data:
    if 'script' in line or 'meta' in line or 'link' in line :
        line=re.split('<script>|</script> | <meta>|</meta> | <link> | </link>' , line)
        for x in line:
            if '://' in x:
                temp=x.split('://')[1]
                dataset.append(temp.split('/')[0])
        #dataset.append(line)

for x in dataset:
    print (x)

