"""
Main.py All functions & Libraries to run go here
"""
import os   #imports OS features
import urllib #Requests a URL
import io
from tld import get_tld     #Extracts the top level domains from URL


def main():
    banner()


"""
Banner Function
"""

def banner():
    print("******************************\n"
          "              ^               \n"                                         
          "             | |              \n"                                        
          "             |V|              \n"                                                 
          "             |A|              \n"                                        
          "           _||L||_            \n"                                              
          "           |  I  |            \n"                                            
          "           \  A  /            \n"                                                          
          "           /  N  \            \n"                                             
          "          /|  T  |\           \n"                            
          "         /    |    \          \n"                                               
          "        /     |     \         \n"                                               
          "      /|      |      |\       \n"                                         
          "     /|       |       |\      \n"                                               
          "    / |       !       | \     \n"                                               
          "   / @|       !       |@ \    \n"                                               
          "  |....  ___  !  ___  ....|   \n"                                              
          "  |__----   \_!_/   ----__|   \n"                                          
          "              V               \n"
          "       Website Scanner        \n"
          "******************************")


"""
Makes a home directory function
"""


def make_home_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

"""
Write file function
"""


def write_to_file(path, output):
    f = open(path, 'w')
    f.write(output)

"""
Gets the domain name from URL
"""


def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name

"""
Get website ip address
"""


def get_ip(url):
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
    command = "nmap "+scan+" "+ip
    execute = os.popen(command)
    nmap = str(execute.read())
    return nmap


"""
Robots Function
"""


def get_robots(url):
    if url.endswith('/'):
        path = url
    else:
        path = 'http://'+url+'/'
    requests = urllib.urlopen(path + "robots.txt", data=None)
    #data = io.TextIOWrapper(requests, encoding='utf-8')
    robots = requests.read()
    return robots



if __name__ == '__main__':
    main()
    print(get_ip("www.itb.ie"))
    print(get_robots("www.itb.ie"))
    print(get_nmap("-sV", get_ip("www.itb.ie")))
