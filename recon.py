import os   # imports OS features
import urllib   # Requests a URL
from tld import get_tld     # Extracts the top level domains from URL

"""
Gets the domain name from URL
"""


def get_domain_name(url):
    print("Obtaining Top Level Domain.....")
    domain_name = get_tld(url)
    return domain_name

"""
Get website ip address
"""


def get_ip(url):
    print("Obtaining IP Address.....")
    command = "host "+url
    execute = os.popen(command)
    result = str(execute.read())
    finder = result.find('has address')+12
    ip = result[finder:].splitlines()[0]
    return ip

"""
NMAP Scan Function
@:param scan Scan Options
@:param ip IP Address
"""


def get_nmap(scan, ip):
    print("Nmap Started Scanning.....")
    command = "nmap "+scan+" "+ip
    execute = os.popen(command)
    nmap = str(execute.read())
    return nmap


"""
Robots Function
"""


def get_robots(url):
    print("Fetching Robots.txt.....")
    if url.endswith('/'):
        path = url
    else:
        path = 'http://'+url+'/'
    requests = urllib.urlopen(path + "robots.txt", data=None)
    robots = requests.read()
    return robots


"""
Whois Function
"""


def get_whois(domain_name):
    print("Fetching Whois Info.....")
    command = "whois "+domain_name
    execute = os.popen(command)
    whois = str(execute.read())
    return whois