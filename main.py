"""
Main.py All functions & Libraries to run go here
"""
from recon import *
from spider import *
from valiant import *


def main():

    banner()
    name = raw_input("[+] Please Enter A Targets Name: ")
    url = raw_input("[+] Please Enter A Targets URL: ")
    print("***************************************************************")
    get_links(name, url)
    print("***************************************************************")
    print("[+] Websites IP:"+get_ip(url))


    read_file("MUTILLIDAE")


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
    #domain_name = get_domain_name(url)
    #ip_address = get_ip(domain_name)
    #robots = get_robots(domain_name)
    #whois = get_whois(domain_name)
    # nmap = get_nmap("-sV", ip_address)
    create_report(name, url)
    #get_links(name, url)

"""
Create Report Function
"""


def create_report(name, url):
#def create_report(name, url, domain_name, ip_address, robots, whois, spider): # ,nmap

    root_folder = 'sites'
    make_home_directory(root_folder)

    target_directory = root_folder+"/"+name
    make_home_directory(target_directory)
    write_to_file(target_directory + "/url.txt", url)
    #write_to_file(target_directory + "/domain.txt", domain_name)
    #write_to_file(target_directory + "/ip.txt", ip_address)
    #write_to_file(target_directory + "/robots.txt", robots)
    #write_to_file(target_directory + "/whois.txt", whois)
    #write_to_file(target_directory + "/nmap.txt", nmap)


if __name__ == '__main__':
    main()
