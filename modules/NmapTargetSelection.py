import subprocess
import sys
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
print("Example : www.testhostname.com")
print(" ")
webbs = input("" + RS + "[" + B + "ENTER TARGET " + R + "WEBSITE " + RS + "]" + G + ": " + RS)
webb = input("" + RS + "[" + B + "ENTER TARGET " + R + "WEBSITE " + Y + "IP" + RS + "]" + G + ": " + RS)
print(" ")
print(R + "[" + G + "Scan a single IP" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', webb])
print(" ")
print(R + "[" + G + "Scan a host" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', webbs])