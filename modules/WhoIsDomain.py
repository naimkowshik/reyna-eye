import os
import time

R = " \033[1;31m"
B = "\033[1;34m"
Y = "\033[1;33m"
RS = "\033[0m"
G = "\033[32m"
W = "\033[1;37m"



print(" ")
target = input(W+"    ["+R+"Domain "+W+"]"+G+": "+RS)
print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mWhois Lookup\033[0m" + R + "By " + Y + "Domain " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m".format(target) + target)
print(" ")
time.sleep(0.5)
command = ("whois " + target)
proces = os.popen(command)
results = str(proces.read())
print("\033[0m" + results + "\033[0m")