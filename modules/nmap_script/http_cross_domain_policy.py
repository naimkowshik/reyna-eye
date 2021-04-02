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
  Checks the cross-domain policy file (/crossdomain.xml) and the client-acces-policy file (/clientaccesspolicy.xml) 
  in web applications and lists the trusted domains. 
  Overly permissive settings enable Cross Site Request Forgery attacks and may allow attackers to access sensitive data. 
  This script is useful to detect permissive configurations and possible domain names available for purchase to exploit the application. 

  The script queries instantdomainsearch.com to lookup the domains. This functionality is turned off by default, 
  to enable it set the script argument http-cross-domain-policy.domain-lookup. 

  References:

    • http://sethsec.blogspot.com/2014/03/exploiting-misconfigured-crossdomainxml.html
    • http://gursevkalra.blogspot.com/2013/08/bypassing-same-origin-policy-with-flash.html
    • https://www.adobe.com/devnet/articles/crossdomain_policy_file_spec.html
    • https://www.adobe.com/devnet-docs/acrobatetk/tools/AppSec/CrossDomain_PolicyFile_Specification.pdf
    • https://www.owasp.org/index.php/Test_RIA_cross_domain_policy_%28OTG-CONFIG-008%29
    • http://acunetix.com/vulnerabilities/web/insecure-clientaccesspolicy-xml-file

""")
webb = input("" + RS + "[" + B + "ENTER TARGET " + R + "WEBSITE " + Y + "IP" + RS + "]" + G + ": " + RS)
print(" ")
subprocess.check_call(['nmap', '-p', '80', '--script', 'http-cross-domain-policy', webb])