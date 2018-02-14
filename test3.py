import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup


def changerankscrapper(site):
    """
    Takes a site url, scrapes that site's Alexa page,
    and returns the site's global Alexa rank and the
    change in that rank over the past three months.
    """

    #Create Alexa URL
    url = "http://www.alexa.com/siteinfo/" + site

    #Get HTML
    cj = cookielib.CookieJar()
    mech = mechanize.OpenerFactory().build_opener(mechanize.HTTPCookieProcessor(cj))
    request = mechanize.Request(url)
    response = mech.open(request)
    html = response.read()

    #Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html)

    globalrank = int(soup.find("strong", { "class" : "metricsUrl font-big2 valign" }).text)
    changerank = int(soup.find("span", { "class" : "change-wrapper change-up" }).text)


    return globalrank, changerank

#Example
site = "http://stackoverflow.com/"
globalrank, changerank = changerankscrapper(site)
print(globalrank)
print(changerank)