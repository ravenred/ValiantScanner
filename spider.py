"""
spider.py used to gather all internal links
"""
import urllib
import re


def get_links(name, url):

    root_folder = 'sites'
    path = root_folder + "/" + name + "/" + "crawled.txt"

    f = open(path, 'w')

    print("Spider Started....")
    requests = urllib.urlopen(url, data=None)
    links = requests.read()

    find_links = re.findall('<a href="(.*?)">', str(links))     # Uses re library to find all href sources

    # path = "targets/"+name+"/links.txt"
    # f = open(path, 'w')
    url_list = []

    for a in find_links:
        if "http" not in a:
            if "mailto:" not in a:

                    sub_url = a.split(" ")[0]  # Deletes all characters after whitespace
                    fullurl = url+sub_url
                    url_list.append(fullurl)

    for i in url_list:

        requests = urllib.urlopen(i, data=None)
        links = requests.read()
        print(i)
        print(requests.code)

        find_links = re.findall('<a href="(.*?)">', str(links))
        for b in find_links:
            if "http" not in b:
                if "mailto:" not in b:
                    sub_url = b.split(" ")[0]  # Deletes all characters after whitespace
                    fullurl = url + sub_url
                    if fullurl not in url_list:
                        url_list.append(fullurl)

    for x in url_list:
        f.write(x+"\n")

    print("Spider Stopping....")

#get_links("http://itb.ie")