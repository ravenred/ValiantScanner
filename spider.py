"""
spider.py used to gather all internal links
"""
import urllib
import re


def get_links(url):

    print("Spider Started....")
    requests = urllib.urlopen(url, data=None)
    links = requests.read()
    # print(requests.status)

    find_links = re.findall('<a href="(.*?)">', str(links))     # Uses re library to find all href sources

    for a in find_links:
        if "http" not in a:
            if "mailto:" not in a:

                    sub_url = a.split(" ")[0]  # Deletes all characters after whitespace
                    fullurl = url+sub_url
                    return fullurl
