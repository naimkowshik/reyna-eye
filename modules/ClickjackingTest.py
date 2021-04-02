#!/usr/bin/env/python3

import time
import os


#############################
R = "\033[1;31m"            #
B = "\033[1;34m"            #
Y = "\033[1;33m"            #
G = "\033[32m"              #
RS = "\033[0m"              #
W = "\033[1;37m"            #
#############################

os.system("clear")
print("\n\033[1;31m[\033[1;33mi\033[1;31m]\033[0m" + R + " Clickjacking " + Y + "Test " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
target = input("\n "+W+"["+R+"Domain "+W+"]"+G+": "+RS)
if not (target.startswith("http://") or target.startswith("https://")):
    target = "http://" + target
print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m".format(target) + target)

time.sleep(0.5)
try:
    from pip._vendor import requests

    resp = requests.get(target)
    headers = resp.headers
    print("\nHeader set are: \n")
    for item, xfr in headers.items():
        print("\033[0m" + item + ":" + xfr + "\033[0")

    if "X-Frame-Options" in headers.keys():
        print("\n \033[1;31m[\033[1;33m❌\033[1;31m]\033[0m \033[1;33mClick Jacking Header is Present \033[0m")
        print(" \033[1;31m[\033[1;33m❌\033[1;31m]\033[0m \033[1;33m! \033[1;31mYou can't clickjack this site \033[1;33m! \033[0m")
        print(" ")
    else:
        facesmiling = '\U0001F600'
        print("\n" + R + "[" + facesmiling + "]""\033[32mX-Frame-Options-Header is missing \033[1;33m! \033[1;m")
        print(R + "[" + facesmiling + "]""\033[32mClickjacking is possible,\033[1;31mthis site is vulnerable to Clickjacking\033[1;m\n")
        print(" ")
except Exception as ex:
    print("\033[1;34mException caught: " + str(ex))