import urllib2



usock = urllib2.urlopen(url)
data = usock.read()
usock.close()



f=open('data.html','w')
f.write(data)
print len(data)
f.close()

