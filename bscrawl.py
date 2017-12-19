from bs4 import BeautifulSoup
import sys
import requests

def get_links(url):

    r = requests.get(url)
    contents = r.content

    soup = BeautifulSoup(contents, 'lxml')
    links = []
    for link in soup.findAll('a'):
        try:
            links.append(link['href'])
        except KeyError:
            pass
    return links

if __name__ == "__main__":
    url = "http://www.itb.ie"
    print get_links(url)
    sys.exit()