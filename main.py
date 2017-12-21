"""
Main.py All functions & Libraries to run go here
"""
from recon import *
from spider import *


def main():

    banner()
    name = raw_input("[+] Please Enter A Targets Name: ")
    url = raw_input("[+] Please Enter A Targets URL: ")
    print("***************************************************************")
    create_report(name, url)


"""
Banner Function
"""


def banner():

    print("\033[1;34m***************************************************************\n"
          "*                               ^                             *\n"                                         
          "*                              | |                            *\n"                                        
          "*                              |V|                            *\n"                                                 
          "*                              |A|                            *\n"                                        
          "*                            _||L||_                          *\n"                                              
          "*                            |  I  |                          *\n"                                            
          "*                            \  A  /                          *\n"                                                          
          "*                            /  N  \                          *\n"                                             
          "*                           /|  T  |\                         *\n"                            
          "*                          /    |    \                        *\n"                                               
          "*                         /     |     \                       *\n"                                               
          "*                       /|      |      |\                     *\n"                                         
          "*                      /|       |       |\                    *\n"                                               
          "*                     / |       !       | \                   *\n"                                               
          "*                    / @|       !       |@ \                  *\n"                                               
          "*                   |....  ___  !  ___  ....|                 *\n"                                              
          "*                   |__----   \_!_/   ----__|                 *\n"                                          
          "*                               V                             *\n"
          "*                        Website Scanner                      *\n"
          "***************************************************************\033[1;m")


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
Report Findings function
"""


def report_findings(name, url):

    print("hi")


"""
Create Report Function
"""


def create_report(name, url):

    root_folder = 'sites'
    make_home_directory(root_folder)

    target_directory = root_folder+"/"+name
    make_home_directory(target_directory)
    print("***************************************************************")
    print("[+] Websites IP:"+get_ip(url))
    print("***************************************************************")
    print("[+] Whois Information")
    print(get_whois(url))
    print("***************************************************************")
    print(get_robots(url))
    print("***************************************************************")
    get_links(name, url)


if __name__ == '__main__':
    main()
