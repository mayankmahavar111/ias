import socket
from urlunshort import is_shortened
from urlparse import urlparse
from urllib2 import urlopen
import whois


url_aadress='google.com'
code = urlopen("http://{}".format(url_aadress)).code
print socket.gethostbyname(url_aadress)
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
x=whois.query(url_aadress)
print x.expiration_date