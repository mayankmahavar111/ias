import urllib,re


def GetPageRank (name):
    xml = urllib.urlopen('http://data.alexa.com/data?cli=10&dat=s&url=%s' % name).read()

    try:
        rank = int(re.search(r'<POPULARITY[^>]*TEXT="(\d+)"', xml).groups()[0])
        print rank
    except Exception as e:
        print e

if __name__ == "__main__" :
    url_name=raw_input("Enter url :")
    print GetPageRank(url_name)