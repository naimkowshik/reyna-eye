import time
import os
banner = """
     \033[1;34m▄▄▌ ▐ ▄▌▄▄▄ .▄▄▌   \033[1;31m▄▄·       • ▌ ▄ ·. ▄▄▄ .
     \033[1;34m██· █▌▐█▀▄.▀·██•  \033[1;31m▐█ ▌▪▪     ·██ ▐███▪▀▄.▀·
     \033[1;34m██▪▐█▐▐▌▐▀▀▪▄██▪  \033[1;31m██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄
     \033[1;34m▐█▌██▐█▌▐█▄▄▌▐█▌▐▌\033[1;31m▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌
      \033[1;34m▀▀▀▀ ▀▪ ▀▀▀ .▀▀▀ ·\033[1;31m▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀ 

 """
print(banner)

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

time.sleep(2)
print(R + "[" + G + " File vulners " + R + "]" + RS)
print(" ")
os.system("wget https://svn.nmap.org/nmap/scripts/vulners.nse -P /usr/share/nmap/scripts")
print(" ")
time.sleep(1)
print(R + "[" + G + " File vulscan " + R + "]" + RS)
print(" ")
os.system("wget https://raw.githubusercontent.com/scipag/vulscan/master/vulscan.nse -P /usr/share/nmap/scripts")
print(" ")
time.sleep(1)
os.system("mkdir /opt/reyna/")
time.sleep(2)
os.system("cp -r /opt/reyna/")
print(" ")
print(R + "[" + G + "Thanks For Setup" + R + "]" + RS)

