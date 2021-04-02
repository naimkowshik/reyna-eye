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
  • Enter Target IP type IP example : 10.7.1.0/24

  • Than ask Enter Port Example : 80,443 or 80
""")
print(" ")
webb = input("" + RS + "[" + B + "ENTER TARGET " + R + "WEBSITE " + Y + "IP" + RS + "]" + G + ": " + RS)
print(" ")
port = input("" + RS + "[" + B + "ENTER TARGET " + R + "WEBSITE " + Y + "PORT" + RS + "]" + G + ": " + RS)
subprocess.check_call(['nmap', '-sT', '-p', port, webb])