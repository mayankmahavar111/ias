import socket
from urlunshort import is_shortened
from urlparse import urlparse
from urllib2 import urlopen
import whois


url_aadress='bit.ly/2rRKIob'

#code = urlopen("http://{}".format(url_aadress)).code
""""
try:
    print socket.gethostbyname(url_aadress)
except:
    print "unable to find host by name"
print len(url_aadress)
print is_shortened(url_aadress),'url shortened'
print '@' in url_aadress,'At the rate   '
print  '//' in url_aadress,'double slash'
print '-' in url_aadress.split('.')[0] ,'dash'
print len(url_aadress.split('.')),'sub domain'
print urlparse(url_aadress),''
print url_aadress.split(':'),'port'
print 'https' in url_aadress

if (code / 100 >= 4):
    print "False"
else:
    print "True"


x=whois.whois(url_aadress)
print x
#print len(x.expiration_date)
"""