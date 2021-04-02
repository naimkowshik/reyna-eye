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
print(R + "[" + G + "Detect OS and Services" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-A', webb])
print(" ")
print(R + "[" + G + "Standard service detection" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-sV', webb])
print(" ")
print(R + "[" + G + "More aggressive Service Detection" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-sV', '--version-intensity', '5', webb])
print(" ")
print(R + "[" + G + "Lighter banner grabbing detection" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-sV', '--version-intensity', '0', webb])