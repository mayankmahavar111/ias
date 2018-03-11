import urllib2


<<<<<<< HEAD
=======

url = 'http://www.reddit.com '
>>>>>>> 44a19a0fab93aa12bc34880995859da83d5bc608

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()



f=open('data.html','w')
f.write(data)
print len(data)
f.close()

