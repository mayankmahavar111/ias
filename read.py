import socket
from urlunshort import is_shortened
from urllib2 import urlopen


positive='1'
negative='-1'
neutral='0'


def getIpaddress(name):
    try:
        socket.gethostbyname(name)
        return positive
    except:
        return negative


def urlLenght(name):
    if len(name) > 54 :
        return negative
    elif len(name)>45 and len(name) <=54:
        return neutral
    else:
        return positive


def shortenUrl(name):
    if is_shortened(name) is True:
        return negative
    else:
        return positive

def atTherate(name):
    if '@' in name:
        return negative
    else:
        return positive

def doubleSlash(name):
    if '//' in name :
        return negative
    else:
        return positive

def dash(name):
    if '-' in name:
        return negative
    else:
        return positive


def subDomain(name):
    if name.count('.') > 2 :
        return negative
    elif name.count('.')>1:
        return neutral
    else:
        return positive


def port(name):
    if len(name.split(':')) ==1 :
        return positive
    name=name.split(':')[1]
    if name is not '80' or  name is not '443' :
        return negative
    else:
        return positive

def https(name):
    if 'https' in name or 'HTTPS' in name :
        return negative
    else:
        return positive

def CodeLength(name):
    code = urlopen("http://{}".format(name)).code
    if (code / 100 >=4):
        return negative
    else:
        return positive


def datasetGenerator(line):
    temp=[]
    temp.append(getIpaddress(line))
    temp.append(urlLenght(line))
    temp.append(shortenUrl(line))
    temp.append(atTherate(line))
    temp.append(doubleSlash(line))
    temp.append(dash(line))
    temp.append(subDomain(line))
    temp.append(port(line))
    temp.append(https(line))
    temp.append(CodeLength(line))
    return ','.join(temp)

if __name__ == '__main__':
    with open('top-1m.csv','r') as f:
        temp=[]
        for line in f.readlines():
            line=line.split(',')[1]
            line=line.split('\n')[0]
            temp=datasetGenerator(line)
            break

    print temp
    print (temp.count('1'))


