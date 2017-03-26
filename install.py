#/usr/bin/python

import os
import sys
from time import sleep

try:
    if sys.argv[1] == "install":
        os.system("mkdir /usr/share/hol")
        sleep(0.2)
        os.system("cp * /usr/share/hol")
        sleep(0.2)
        os.system("rm -rf /usr/share/hol/install.py")
        sleep(0.2)
        file = open("/usr/bin/hol","w")
        file.write("#/usr/bin/bash\n")
        file.write("\n")
        file.write("python /usr/share/hol/hol.py\n")
        file.close()
        os.system("chmod 777 /usr/bin/hol")
except:
    print "Option not select"
    print "Please, use python "+sys.argv[0]+" install"
