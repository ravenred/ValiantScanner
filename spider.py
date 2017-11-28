"""
spider.py used to gather all internal links
"""
import urllib
import re


def get_links(url):

    path = "https://"+url
    requests = urllib.urlopen(path, data=None)
    links = requests.read()
    print(links)

    find_links = re.findall('<a href=(.*?)>', str(links))

    for a in find_links:
        print(a)

    get_links("www.itb.ie")
