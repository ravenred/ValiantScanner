"""
spider.py used to gather all internal links
"""
import urllib
import re


def get_links(name, url):

    print("Spider Started....")
    requests = urllib.urlopen(url, data=None)
    links = requests.read()
    print(requests.info())

    find_links = re.findall('<a href="(.*?)">', str(links))     # Uses re library to find all href sources

    path = "targets/"+name+"/links.txt"
    f = open(path, 'w')

    for a in find_links:
        if "http" not in a:
            if "mailto:" not in a:

                    sub_url = a.split(" ")[0]  # Deletes all characters after whitespace
                    fullurl = url+sub_url
                    f.writelines(fullurl+"\n")
                    # return fullurl


def crawl_robots(name, url):

    print("Crawling robots.txt....")

    path = "targets/"+name+"/robots.txt"
    f = open(path, 'r')

    for line in f:
        request = urllib.urlopen(line, data=None)
        link = request.read()
        print(request.info)

        find_links = re.findall('<a href="(.*?)">', str(link))  # Uses re library to find all href sources

        path = "targets/" + name + "/crawled.txt"
        f = open(path, 'w')

        for a in find_links:
            if "http" not in a:
                if "mailto:" not in a:
                    sub_url = a.split(" ")[0]  # Deletes all characters after whitespace
                    fullurl = url + sub_url
                    f.writelines(fullurl + "\n")






crawl_robots("Google", "https://www.google.com")