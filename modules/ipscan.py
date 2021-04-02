import json
import os
import sys
import time
import urllib.request


R = " \033[1;31m"
B = "\033[1;34m"
Y = "\033[1;33m"
RS = "\033[0m"
G = "\033[32m"
W = "\033[1;37m"
os.system("clear")
print("\n \033[1;31m   [\033[1;33mi\033[1;31m]\033[0m \033[1;33mIP\033[0m" + R + "Address " + Y + "information " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
print(" ")
target = input(W+"    ["+R+"IP "+W+"]"+G+": "+RS)
url = ("http://ip-api.com/json/")
response = urllib.request.urlopen(url + target)
data = response.read()
jso = json.loads(data)
time.sleep(0.5)

print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m" + target + "")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "IP: " + jso["query"] + "\033[0m")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Status: " + jso["status"] + "\033[0m")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Region: " + jso["regionName"] + "\033[0m")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Country: " + jso["country"] + "\033[0m")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "City: " + jso["city"] + "\033[0m")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "ISP: " + jso["isp"] + "\033[0m")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Lat & Lon: " + str(jso['lat']) + " & " + str(jso['lon']) + "\033[0m")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "Zipcode: " + jso["zip"] + "\033[0m")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "TimeZone: " + jso["timezone"] + "\033[0m")
print(" \033[1;31m[\033[1;33mi\033[1;31m]\033[0m " + "\033[34m" + "AS: " + jso["as"] + "\033[0m" + "\n")

print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mWhois Lookup\033[0m" + R + "By " + Y + "IP " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
print(" ")
command = ("whois " + target)
proces = os.popen(command)
results = str(proces.read())
print("\033[0m" + results + "\033[0m")
