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
For each available CPE the script prints out known vulns 
(links to the correspondent info) and correspondent CVSS scores.

Its work is pretty simple:

    • work only when some software version is identified for an open port
    • take all the known CPEs for that software (from the standard nmap -sV output)
    • make a request to a remote server (vulners.com API) to learn whether any known vulns exist for that CPE
    • if no info is found this way, try to get it using the software name alone
    • print the obtained info out

NB: Since the size of the DB with all the vulns is more than 250GB there is no way to use a local db. 
So we do make requests to a remote service. Still all the requests contain just two fields 
the software name and its version (or CPE), so one can still have the desired privacy.
""")
print(" ")
webb = input("" + RS + "[" + B + "ENTER TARGET " + R + "WEBSITE " + Y + "IP" + RS + "]" + G + ": " + RS)
subprocess.check_call(['nmap', '-sV', webb])
time.sleep(2)
subprocess.check_call(['nmap', '--script', 'vulners,vulscan', '-sV', webb])