#######################################################
## This tool is to automatic restart Jenkins jobs ##### 
## which has some specific errors(or error codes)######
#######################################################

import subprocess
import getpass
import urllib
import os
import requests
import sys
"""
pwd=getpass.getpass()
d={'@':'%40','&':'%26'}
for i,j in d.iteritems():
        pwd=pwd.replace(i,j)
"""


#collect all the job names from storage
def jobList():
        cmd ="ls /proj/hudson01/webhome/jobs -1 | grep \'^[L,M,N,O][A-Z].*derivative\' >JobList"
        os.system(cmd)
        print "collection job list is done"
        print "jobs in file: JobList"


def searchWord(filename,keyword):
        with open(filename) as f:
                if keyword in f.read():
                        return True
                else:
                        return False

def checkStatus(job,username,pwd):
        urlx="https://"+username+":"+pwd+"@jenkins.mot.com/job/"+job+"/api/xml?depth=1"
        cmdx="curl "+urlx+" -o temp -s"
        subprocess.call(cmdx,shell=True)
        with open("temp","r") as t:
                if "<building>true</building>" in t.read():
                        return 1
        urlj="https://"+username+":"+pwd+"@jenkins.mot.com/job/"+job+"/api/json?pretty=true"
        cmdj="curl "+urlj+" -o temp -s"
        subprocess.call(cmdj,shell=True)
        with open("temp","r") as t:
                for line in t.readlines():
                        if "\"inQueue\" : true,"  in line:
                                return -1
                        if  "\"buildable\" : false," in line:
                                return 0
                return 2

def restart(job,username,pwd):
	flag=checkStatus(job,username,pwd)
        if flag==2:
#        jname="z_mingjunl_test"
		cmd="curl -k -X POST \"https://"+username+":"+pwd+"@jenkins.mot.com/job/"+job+"/build?delay=0sec\""
		print "start build "+job
		subprocess.call(cmd,shell=True)
	elif flag==1:
		print job+" is building. Can not restart now"
	elif flag==0:
		print job+" is Disabled. Can not restart now"
	elif flag==-1:
		print job+" is InQueue. Can not restart now"

def checkpwd(username,pwd):
	print "checking username and password .................."
        r = requests.head("https://"+username+":"+pwd+"@jenkins.mot.com/")
        status=int(r.status_code)
	return status

if __name__=="__main__":
	username=raw_input("username :")
        pwd=getpass.getpass("password :")
        d={'@':'%40','&':'%26'}
        for i,j in d.iteritems():
                pwd=pwd.replace(i,j)
	if checkpwd(username,pwd) is not 200:
		print "wrong username or password"
		sys.exit()
	else:
		print "Username and Password is good.................." 
	# kewyword is the string that can identify the error. it can be part of the error message or Error code
	keyword=raw_input("keyword of error :").strip()
#        keyword="/obj/ETC/sepolicy.recovery_intermediates/sepolicy.recovery] Error 1"
        jobList()
        with open ("JobList","r") as f:
                for line in f.readlines():
                        job=line.strip()
                        url="curl \"https://"+username+":"+pwd+"@jenkins.mot.com/job/"+job+"/lastBuild/logText/progressiveText?start=0\" -o console -s"
                        subprocess.call(url,shell=True)
#			for item in keyword:
                        if searchWord("console",keyword):
				link="https://jenkins.mot.com/job/"+job
				print link+" has error: "+ keyword
				restart(job,username,pwd)
#				break
                        else:
                                print job+" does not meet error"
