import urllib2

url = 'https://d20kve05iondkm.cloudfront.net/assets/light-vendor-7bb162d30fe5a345edfc448eba5aae1d.js' # write the url here

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()



f=open('data.html','w')
f.write(data)
print len(data)
f.close()

