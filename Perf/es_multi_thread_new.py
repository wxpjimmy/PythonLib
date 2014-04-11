from ElasticsearchClient import ES
from utils import timeit
from extract import parsewpxml
from Queue import Queue
import time
from threading import Thread
import os
from bz2 import BZ2File
import sys

q = Queue()
num_threads = 8
es = ES({"localhost":"9200"}, 'wiki', 'all')
total = 0

def test_handler(page):
    pass


def page_handler(page):
    """Write the right bits to the right files."""
    global total
    if total == 100000:
        print("End: %f" % (time.time()))
        pass
    else:
        for rev in page['revisions']:
            q.put([page['title'], rev['text'], rev['timestamp']])
            total += 1

def Worker():
    count = 0
    while True:
        try:
            item = q.get(block=True, timeout=30)
            es.index(item[0], item[1])
            count += 1
            q.task_done
            print("index-Num: %d" % (count))
        except Exception, e:
            print e
            break
    print("Finishe processing %d, time: %f" % (count, time.time()))


def main(argv=None, input=sys.stdin):
#    FILE = os.path.join(os.path.dirname(__file__), 'test.xml')
#    path =  os.path.join(os.path.dirname(__file__), 'test.xml.bz2')
#path =  os.path.join(os.path.dirname(__file__), 'enwiki-20140203-pages-articles-multistream.xml.bz2')
    for i in range(num_threads):
        t = Thread(target=Worker)
        t.daemon = True
        t.start()
    print("Start: %f" %  (time.time()))
    parsewpxml(input, page_handler)
    q.join()

if __name__ == '__main__':
    main()
