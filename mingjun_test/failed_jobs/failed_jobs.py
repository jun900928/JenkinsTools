#############################################################
##  This tool is to find the most recent failed jobs       ##
##  But it also can be used to the following reasons:	   ##
##  1. check the failed jobs with specifiy failed errors   ##
##  2. check the failed jobs with or without take any      ##
##     actions						   ##
#############################################################

import subprocess
import getpass
import urllib
import os


def jobList():
        cmd ="ls /proj/hudson01/webhome/jobs -1>JobList"
        os.system(cmd)
        print "collection job list is done"

def searchWord(filename,keyword):
        with open(filename) as f:
		if keyword in f.read():
			return line
	        else:
			return False


def checkStatus(job):
        urlx="https://"+user+":"+pwd+"@jenkins.mot.com/job/"+job+"/api/xml?depth=1"
        cmdx="curl "+urlx+" -o temp -s"
        subprocess.call(cmdx,shell=True)
        with open("temp","r") as t:
                if "<building>true</building>" in t.read():
                        return 1
        urlj="https://"+user+":"+pwd+"@jenkins.mot.com/job/"+job+"/api/json?pretty=true"
        cmdj="curl "+urlj+" -o temp -s"
        subprocess.call(cmdj,shell=True)
        with open("temp","r") as t:
                for line in t.readlines():
                        if "\"inQueue\" : true,"  in line:
                                return -1
                        if  "\"buildable\" : false," in line:
                                return 0
                return 2

if __name__=="__main__":
#	pwd=''.decode('base64')
	user=raw_input("username :")
	pwd=getpass.getpass("password :")
        d={'@':'%40','&':'%26'}
        for i,j in d.iteritems():
                pwd=pwd.replace(i,j)
# keyword is the failed error if it is 'Finished: FAILURE', then it will check all the failed jobs	
	keyword="fatal: Couldn't find remote ref refs/tags/MPB24.22-TITAN-SHA1"
	jobList()
        with open ("JobList","r") as f:
                for line in f.readlines():
                        job=line.strip()
			if job[0].islower() or 'tag' in job:
				continue
                        url="curl \"https://"+user+":"+pwd+"@jenkins.mot.com/job/"+job+"/lastBuild/logText/progressiveText?start=0\" -o console -s"
			subprocess.call(url,shell=True)
			if searchWord("console",keyword):
				flag=checkStatus(job)
# modify the conditions with the flag,  get jobs in different conditions
				if flag==2:
					link="https://jenkins.mot.com/job/"+job
                                        print link + " : "+keyword
#				elif flag==0:
#					print job+" is disabled"
#				elif flag==1 or flag==-1:
#					print job+" is taken care"
#			else:
#				print job
