"""
In somehow, the job's configure file is gone 
in the local directory.This tool is to 
refresh the config.xml
"""

import subprocess
import getpass
import urllib

username=raw_input("username :")
pwd=getpass.getpass("password :")
d={'@':'%40','&':'%26'}
for i,j in d.iteritems():
        pwd=pwd.replace(i,j)
url = "curl -k -X POST \"https://"+user+":"+pwd+"@jenkins.mot.com/job/"

def status(job):
        urlj="https://"+user+":"+pwd+"@jenkins.mot.com/job/"+job+"/api/json?pretty=true"
        cmdj="curl "+urlj+" -o temp -s"
        subprocess.call(cmdj,shell=True)
        with open("temp","r") as t:
                for line in t.readlines():
                        if  "\"buildable\" : false," in line:
                                return False
                return True



def enable(job):
	cmd=url+job+"/enable\""
	subprocess.call(cmd,shell=True)
def disable(job):
	cmd=url+job+"/disable\""
	subprocess.call(cmd,shell=True)

if __name__=="__main__":
	with open("joblist") as jobs:
		for job in jobs.readlines():
			job=job.strip()
			flag=status(job)
			if flag:
#				print "enable"
				disable(job)
				enable(job)
			else:
#				print "disable"
				enable(job)
				disable(job)
			print job+" is done"
