import urllib2

<<<<<<< HEAD
url = 'https://d20kve05iondkm.cloudfront.net/assets/light-vendor-7bb162d30fe5a345edfc448eba5aae1d.js' # write the url here
=======
url = 'http://emiratesnbd.deralreserve.com' # write the url here
>>>>>>> 387face1aa5b95064e297f95bdba4a5c0b66036e

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()



f=open('data.html','w')
f.write(data)
print len(data)
f.close()

