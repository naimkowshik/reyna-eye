import time
import os

R = " \033[1;31m"
B = "\033[1;34m"
Y = "\033[1;33m"
RS = "\033[0m"
G = "\033[32m"
W = "\033[1;37m"


os.system("clear")
print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[1;33mHTTP\033[0m" + R + "Header " + Y + "Grabber " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
target = input("\n"+W+"["+R+"Domain "+W+"]"+G+": "+RS)
https_or_http = input("\n\033[1;31m[\033[1;33m!\033[1;31m]\033[0m \033[1;33mHTTPS\033[0m\033[1;34m Or\033[1;33m HTTP\033[1;31m[\033[1;33m!\033[1;31m]\033[1;31m: \033[0m")
print("\n \033[1;31m[\033[1;33m+\033[1;31m]\033[0m \033[1;33mUrl\033[1;31m: \033[0m" + target + "")
print(" ")
time.sleep(1.5)
command = (https_or_http + " -v " + target)
proces = os.popen(command)
results = str(proces.read())
print("\033[0m" + results + "\033[0m")