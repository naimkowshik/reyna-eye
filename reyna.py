#!/usr/bin/env/python3

import sys
from urllib.error import URLError
import dns.resolver  # Installed packages: 'dnspython'
import json
import subprocess
import time
import urllib.request
import os
from time import gmtime, strftime
from urllib.error import URLError
from urllib.parse import urlsplit
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

#############################
#    COLORING YOUR SHELL    #
#############################
R = "\033[1;31m"            #
B = "\033[1;34m"            #
Y = "\033[1;33m"            #
G = "\033[1;32m"            #
RS = "\033[0m"              #
W = "\033[1;37m"            #
#############################
os.system("clear")
banner = """
     \033[1;34m██████\033[1;37m╗ \033[1;34m███████\033[1;37m╗\033[1;34m██\033[1;37m╗   \033[1;34m██\033[1;37m╗\033[1;34m███\033[1;37m╗   \033[1;34m██\033[1;37m╗ \033[1;34m█████\033[1;37m╗   \033[1;31m██████\033[1;37m╗     \033[1;31m██████\033[1;37m╗ 
     \033[1;34m██\033[1;37m╔══\033[1;34m██\033[1;37m╗\033[1;34m██\033[1;37m╔════╝╚\033[1;34m██\033[1;37m╗ \033[1;34m██\033[1;37m╔╝\033[1;34m████\033[1;37m╗  \033[1;34m██\033[1;37m║\033[1;34m██\033[1;37m╔══\033[1;34m██\033[1;37m╗   \033[1;37m╚════\033[1;31m██\033[1;37m╗  \033[1;31m██\033[1;37m╔═\033[1;31m████\033[1;37m╗
     \033[1;34m██████\033[1;37m╔╝\033[1;34m█████\033[1;37m╗   ╚\033[1;34m████\033[1;37m╔╝ \033[1;34m██\033[1;37m╔\033[1;34m██\033[1;37m╗ \033[1;34m██\033[1;37m║\033[1;34m███████\033[1;37m║    \033[1;31m█████\033[1;37m╔╝  \033[1;31m██\033[1;37m║\033[1;31m██\033[1;37m╔\033[1;31m██\033[1;37m║
     \033[1;34m██\033[1;37m╔══\033[1;34m██\033[1;37m╗\033[1;34m██\033[1;37m╔══╝    ╚\033[1;34m██\033[1;37m╔╝  \033[1;34m██\033[1;37m║╚\033[1;34m██\033[1;37m╗\033[1;34m██\033[1;37m║\033[1;34m██\033[1;37m╔══\033[1;34m██\033[1;37m║  \033[1;31m██\033[1;37m╔═══╝    \033[1;31m████\033[1;37m╔╝\033[1;31m██\033[1;37m║
     \033[1;34m██\033[1;37m║  \033[1;34m██\033[1;37m║\033[1;34m███████\033[1;37m╗   \033[1;34m██\033[1;37m║   \033[1;34m██\033[1;37m║ ╚\033[1;34m████\033[1;37m║\033[1;34m██\033[1;37m║  \033[1;34m██\033[1;37m║  \033[1;31m███████\033[1;37m╗\033[1;34m██\033[1;37m╗╚\033[1;31m██████\033[1;37m╔╝
     \033[1;37m╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚══════╝╚═╝ ╚═════╝ """
print(" ")
print(banner)
print("    " + R + "[" + B + "Twitter" + R + "]" + Y + ":" + G + "[" + R + "@K0WSHIK" + G + "]" + "  " + R + "[" + B + "Github" + R + "]" + Y + ":" + G + "[" + R + "naimkowshik" + G + "]" + "  " + R + "[" + B + "website" + R + "]" + Y + ":" + G + "[" + R + "No Website" + G + "]" + RS)
def yesornot():
    yes_Or_Not = input("\n" + B + "Scanning Complete. " + Y + "Press " + G + "Enter To Continue " + W + "OR " + R + "CTRL + C To Stop" + RS)
    if yes_Or_Not == '':
        os.system("clear")
        print(banner)
        mainMenu()

no_www_https_or_https = G + "Example" + R + ": " + G + "example.com" 

def mainMenu():
    print("     ")
    print("    "+W+"["+G+"+"+W+"] " + Y + "Options " + W + ":" + RS + "                                  "+W+"["+G+"+"+W+"]" + Y + " Nmap Scanner Options " + W + ":" + RS)
    print("     "+W+"└["+R+"•"+W+"]"+G+" 1."+W+" IP Address information" + "                 "+W+"└["+R+"•"+W+"]"+G+" 11."+W+" Nmap Target Selection" + RS)
    print("     " + W + "└[" + Y + "•" + W + "]" + G + " 2." + W + " Who Is Domain Scan" + "                     " + W + "└["+Y+"•"+W+"]"+G+" 12."+W+" Nmap Port Selection All Port Scan" + RS)
    print("     " + W + "└[" + B + "•" + W + "]" + G + " 3." + W + " Robot Txt Scan" + "                         " + W + "└["+B+"•"+W+"]"+G+" 13."+W+" Nmap Port Scan TCP, TCP SYN, UDP, ignore discovery" + RS)
    print("     " + W + "└[" + G + "•" + W + "]" + G + " 4." + W + " HTTP Header Grabber" + "                    " + W + "└["+G+"•"+W+"]"+G+" 14."+W+" Nmap Service and OS Detection All Os Scanner One tools" + RS)
    print("     " + W + "└[" + R + "•" + W + "]" + G + " 5." + W + " Dns Map")
    print("     " + W + "└[" + Y + "•" + W + "]" + G + " 6." + W + " DNS Recon And Enumerating SRV Records" + RS + " "+W+"["+G+"+"+W+"] " + Y + "Nmap " + R + "Vulnerability " + Y + "And " + R + "Script " + Y + "Scanning Options " + W +  ":" + RS)
    print("     " + W + "└[" + B + "•" + W + "]" + G + " 7." + W + " Clickjacking Test" + "                      " + W + "└["+R+"•"+W+"]"+G+" 15."+W+" Nmap " + G + "vulners " + W + "And" + G + " vulscan" + W + " Scanner" + RS)
    print("     " + W + "└[" + G + "•" + W + "]" + G + " 8." + W + " Website WhatWeb Scan " + "                  " + W + "└["+B+"•"+W+"]"+G+" 16."+W+" Nmap " + W + "address-info " + G + "IPv6" + Y + "," + G + "MAC " + Y + "or " + G + "IPv4" + RS)
    print("     " + W + "└[" + R + "•" + W + "]" + G + " 9." + W + " Link Grabber " + "                          " + W + "└["+Y+"•"+W+"]"+G+" 17."+W+" Nmap " + W + "Target Single " + G + "PORT " + W + "Scan" + RS)
    print("     " + W + "└[" + Y + "•" + W + "]" + G + " 10." + W + " Scan Website Traceroute " + "              " + W + "└["+Y+"•"+W+"]"+G+" 18."+W+" Nmap " + W + "Http Cross Domain " + G + "Policy" + RS)
    print(" ")
    choice = int(input("\n"+W+"     ┌["+G+"+"+W+"]Choose the options\n"+W+"     └["+R+"root"+W+"@"+W+G+"reyna"+W+"]:~# "))
    if choice == 1:
        from modules import ipscan
        print(ipscan)
        yesornot()
    elif choice == 2:
        from modules import WhoIsDomain
        print(WhoIsDomain)
        yesornot()
    elif choice == 3:
        from modules import RobotTXTSCAN
        print(RobotTXTSCAN)
        yesornot()
    elif choice == 4:
        from modules import HTTPHeaderGrabber
        print(HTTPHeaderGrabber)
        yesornot()
    elif choice == 5:
        from modules import dnsmap
        print(dnsmap)
        yesornot()
    elif choice == 6:
        from modules import dnsreconandsrv
        print(dnsreconandsrv)
        yesornot()
    elif choice == 7:
        from modules import ClickjackingTest
        print(ClickjackingTest)
        yesornot()
    elif choice == 8:
        from modules import whatweb
        print(whatweb)
        yesornot()
    elif choice == 9:
        from modules import LinkGrabber
        print(LinkGrabber)
        yesornot()
    elif choice == 10:
        from modules import traceroute
        print(traceroute)
        yesornot()
    elif choice == 11:
        from modules import NmapTargetSelection
        print(NmapTargetSelection)
        yesornot()
    elif choice == 12:
        from modules import NmapPortSelection
        print(NmapPortSelection)
        yesornot()
    elif choice == 13:
        from modules import Nmap_Port_Scan_types
        print(Nmap_Port_Scan_types)
        yesornot()
    elif choice == 14:
        from modules import Service_and_OS_Detection
        print(Service_and_OS_Detection)
        yesornot()
    elif choice == 15:
        from modules.nmap_script import vulners_vulscan
        print(vulners_vulscan)
        yesornot()
    elif choice == 16:
        from modules.nmap_script import address_info
        print(address_info)
        yesornot()
    elif choice == 17:
        from modules.nmap_script import target_port_scan
        print(target_port_scan)
        yesornot()
    elif choice == 18:
        from modules.nmap_script import http_cross_domain_policy
        print(http_cross_domain_policy)
        yesornot()



if __name__== "__main__":
    mainMenu()