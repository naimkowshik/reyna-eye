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
print(R + "[" + G + "Scan using TCP connect" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-sT', webb])
print(" ")
print(R + "[" + G + "Scan using TCP SYN scan (default)" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-sS', webb])
print(" ")
print(R + "[" + G + "Scan UDP ports" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-sU', '-p', '123,161,162', webb])
print(" ")
print(R + "[" + G + "Scan selected ports - ignore discovery" + R + "]" + RS)
print(" ")
subprocess.check_call(['nmap', '-Pn', '-F', webb])