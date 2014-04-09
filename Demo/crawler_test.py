import urllib2
from bs4 import BeautifulSoup
import utils
from utils import timeit
import socket
import ElasticsearchClient
from ElasticsearchClient import ES

root = 'http://news.msn.com'
sections = ['/science-technology/', '/us/', '/crime-justice/', '/world/', '/pop-culture/', '/in-depth/', '/offbeat/']
#sections = ['/science-technology/']

def get_content(url):
    try:
        print 'crawling page: ' + url
        f = urllib2.urlopen(url, timeout = 200)
        code = f.getcode()
        if code < 200 or code >= 300:
            print('get page %s failed, error code %d' % (url, code))
            return None
        return f.read()
    except Exception, e:
        if isinstance(e, urllib2.HTTPError):
            print 'http error: {0}'.format(e.code)
        elif isinstance(e, urllib2.URLError) and isinstance(e.reason, socket.timeout):
            print 'url error: socket timeout {0}'.format(e.__str__())
        else:
            print 'misc error: ' + e.__str__()
        return None

get = timeit(get_content)
count = 0
es = ES({"localhost":"9200"}, 'test', 'web')
index = timeit(es.index)

def crawl_sec(sec):
    url = root + sec
    data = get(url)
    if data is not None:
        soup = BeautifulSoup(data)
        links = soup.find_all('a')
        for link in links:
            hre = link.get('href')
            if hre.startswith(sec) and hre != sec:
                lk = root + hre
                pd = get(lk)
                if pd is not None:
                    index(lk, pd)
                    print('crawl page [%s] succeed!' % (lk))

crawl = timeit(crawl_sec)

for sec in sections:
    crawl(sec)


