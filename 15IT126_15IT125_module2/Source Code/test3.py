import urllib2



url = 'http://www.reddit.com '

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()



f=open('data.html','w')
f.write(data)
print len(data)
f.close()

