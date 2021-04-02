import os
import subprocess


R = "\033[1;31m"
B = "\033[1;34m"
Y = "\033[1;33m"
RS = "\033[0m"
G = "\033[32m"
W = "\033[1;37m"

os.system("clear")
print("\n \033[1;31m[\033[1;33mi\033[1;31m]\033[0m \033[0m" + R + "Domain " + Y + "information " "\033[1;31m[\033[1;33mi\033[1;31m]\033[0m")
print("\n"+W+" Note : "+R+"Type Domain With out "+G+"www "+Y+"or "+G+"https "+Y+"or "+G+"https "+RS)
print("\n"+W+" Example : "+G+"example.com"+RS)
target = input("\n"+W+"["+R+" Domain "+W+"]"+G+": "+RS)
subprocess.check_call(["whatweb", target])