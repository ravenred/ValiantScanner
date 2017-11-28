"""
spider.py used to gather all internal links
"""
import urllib
import re


def get_links(url):

    path = "https://"+url
    requests = urllib.urlopen(path, data=None)
    links = requests.read()
    # print(requests.status)

    find_links = re.findall('<a href="(.*?)">', str(links))     # Uses re library to find all href sources

    for a in find_links:

            print(a.split(" ")[0])  # Deletes all characters after whitespace


get_links("www.itb.ie")
