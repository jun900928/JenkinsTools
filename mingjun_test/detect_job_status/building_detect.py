#######################################
## This tool is to detect the job status
#######################################

import subprocess
import getpass
import urllib


user=raw_input("Usernamw :")
pwd=getpass.getpass()
d={'@':'%40','&':'%26'}
for i,j in d.iteritems():
        pwd=pwd.replace(i,j)
url="https://"+user+":"+pwd+"@jenkins.mot.com/job/z_mingjunl_test/api/xml?depth=1"

cmd="curl "+url+"  --output temp"
print cmd
subprocess.call(cmd,shell=True)



with open("temp","r") as t:
	if "<building>true</building>" in t.read():
		print "building"
	else:
		print "not building"
