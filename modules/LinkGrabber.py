import os
import time
from collections import deque
from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup

R = "\033[1;31m"            #
B = "\033[1;34m"            #
Y = "\033[1;33m"            #
G = "\033[32m"              #
RS = "\033[0m"              #
W = "\033[1;37m"            #

os.system("clear")
print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mDomain \033[0m" + R + "Link " + Y + "Grabber " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
print(" ")
target = input("" + RS + "[" + B + " ENTER " + R + "Domain " + RS + "]" + G + ": " + RS).lower()
os.system("reset")
print("\n"+R+"Scanning "+Y+"Link Grabber "+R+" : " + RS + target)
time.sleep(2)
if not (target.startswith("http://") or target.startswith("https://")):
    target = "http://" + target
deq = deque([target])
pro = set()

try:
    while len(deq):
        url = deq.popleft()
        pro.add(url)
        parts = urlsplit(url)
        base = "{0.scheme}://{0.netloc}".format(parts)

        print("[✌] Find URL " + "\033[34m" + url + "\033[0m")
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        soup = BeautifulSoup(response.text, "lxml")
        for anchor in soup.find_all("a"):
            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
            if link.startswith("/"):
                link = base + link
            if not link in deq and not link in pro:
                deq.append(link)
            continue

except KeyboardInterrupt:
    print("\n")
    print("[-] User Interruption Detected..!")
    time.sleep(1)
    print("\n \t\033[34m[!] I like to See Ya, Hacking Anywhere ..!\033[0m\n")


except Exception:
    pass