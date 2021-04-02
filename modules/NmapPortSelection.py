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
webb = input("" + RS + "[" + B + "ENTER TARGET " + R + "WEBSITE " + Y + "IP" + RS + "]" + G + ": " + RS)
print(" ")
print(R + "[" + G + "Scan a single Port" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-p', '22', webb])
print(" ")
print(R + "[" + G + "Scan a range of ports 1-100" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-p', '1-100', webb])
print(" ")
print(R + "[" + G + "Scan 100 most common ports (Fast)" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-F', webb])
print(" ")
print(R + "[" + G + "Scan all 65535 ports" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-p-', webb])
