#!/usr/bin/env python
"""import urllib, sys, re
temp='stackoverflow.com'
xml = urllib.urlopen('http://data.alexa.com/data?cli=10&dat=s&url=%s'%temp).read()
try: rank = int(re.search(r'<POPULARITY[^>]*TEXT="(\d+)"', xml).groups()[0])
except Exception as e:
    print e
    rank = -1
print 'Your rank for %s is %d!\n' % (temp, rank)
"""