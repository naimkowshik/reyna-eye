import subprocess
import sys
import time
import os

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
print(" ")
print(R + "[" + G + "User Summary " + R + "]" + RS)
print("""
 Shows extra information about IPv6 addresses, such as embedded MAC or IPv4 addresses when available.

 Some IP address formats encode extra information; for example some IPv6 addresses encode an IPv4 address or MAC address
 script can decode these address formats: 

 • IPv4-compatible IPv6 addresses, 
 • IPv4-mapped IPv6 addresses, 
 • Teredo IPv6 addresses, 
 • 6to4 IPv6 addresses, 
 • IPv6 addresses using an EUI-64 interface ID, 
 • IPv4-embedded IPv6 addresses, 
 • ISATAP Modified EUI-64 IPv6 addresses. 
 • IPv4-translated IPv6 addresses and 

 See RFC 4291 for general IPv6 addressing architecture and the definitions of some terms.
""")
print(" ")
webb = input("" + RS + "[" + B + "ENTER TARGET " + R + "WEBSITE " + Y + "IP" + RS + "]" + G + ": " + RS)
subprocess.check_call(['nmap', '-sV', '-sC', webb])
