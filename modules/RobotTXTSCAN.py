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
G = "\033[32m"              #
RS = "\033[0m"              #
W = "\033[1;37m"            #
#############################
no_www_https_or_https = G + "Example" + R + ": " + G + "example.com" 
print("\n     \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mRobots\033[0m" + R + "TXT " + Y + "Scanner " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
print(" ")
print("         "+no_www_https_or_https)
print(" ")
target = input(W+"    ["+R+" Domain "+W+"]"+G+": "+RS)
print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m" + target + "")
print(" ")
time.sleep(0.5)

if not (target.startswith("http://") or target.startswith("https://")):
    target = "http://" + target
robot = target + "/robots.txt"

try:
    bots = urlopen(robot).read().decode("utf-8")
    print("\033[37m" + (bots) + "\033[0m")
except URLError:
    print("\033[1;31m[-] Can\'t access to {page}!\033[1;m".format(page=robot))

except Exception as ex:
    print("\033[1;34mException caught: " + str(ex))