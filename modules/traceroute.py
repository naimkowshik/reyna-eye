import subprocess

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
no_www_https_or_https = G + "Example" + R + ": " + G + "example.com" 
print(" ")
print("         "+no_www_https_or_https)
print(" ")
webb = input("" + RS + "[" + B + "ENTER TARGET " + R + "WEBSITE " + RS + "]" + G + ": " + RS)
subprocess.check_call(['traceroute',webb])