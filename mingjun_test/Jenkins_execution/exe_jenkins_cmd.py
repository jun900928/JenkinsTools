"""
This tool is to realise the functions the same with Jenkins UI
including:
	1:Build_now
	2:Delete
	3:Stop Last Build
	4:Wipe Workspace
	5:Rebuild The Last
	6:Rename
***
This tool can NOT do any actions on the pending jobs or the jobs are already in the queue



"""

import subprocess
import getpass
import urllib
import requests
import sys

#the directory of jobs in local server
path ='/proj/hudson01/webhome/jobs/'
# the file store the job list
f=open("job_list.txt","r")

user=raw_input("username :")
pwd=getpass.getpass("password :")
d={'@':'%40','&':'%26'}
for i,j in d.iteritems():
	pwd=pwd.replace(i,j)
print "checking username and password........"
r = requests.head("https://"+user+":"+pwd+"@jenkins.mot.com/")
status=int(r.status_code)
if status is not 200:
	print "wrong username and password"
	sys.exit()
url = "curl -k -X POST \"https://"+user+":"+pwd+"@jenkins.mot.com/job/"
#print url

def Build_now():
	for job in f.readlines():
		jname=job.rstrip()
		flag=Building(jname)
		if flag==2:
#        jname="z_mingjunl_test"
			cmd=url+jname+"/build?delay=0sec\""
			print "start build "+jname
			subprocess.call(cmd,shell=True)
		elif flag==1:
                        print jname+" is building. Can not build now"
		elif flag==0:
                        print jname+" is Disabled. Can not build now"
		elif flag==-1:
			print jname+" is InQueue. Can not build now"


def Building(job):
	urli="https://"+user+":"+pwd+"@jenkins.mot.com/job/"+job+"/api/xml?depth=1"
	cmdi="curl "+urli+" -o temp -s"
	subprocess.call(cmdi,shell=True)
	with open("temp","r") as t:
	        if "<building>true</building>" in t.read():
			return 1
	urlj="https://"+user+":"+pwd+"@jenkins.mot.com/job/"+job+"/api/json?pretty=true"
	cmdi="curl "+urlj+" -o temp -s"
        subprocess.call(cmdi,shell=True)
        with open("temp","r") as t:
		for line in t.readlines():
			if "\"inQueue\" : true,"  in line:
                        	return -1
			if  "\"buildable\" : false," in line:
				return 0
		return 2

def Delete():
	print "************PLEASE NOTE**************"
	print "*******Delete is unrecoverable*******"
	decision = raw_input("Do you want to delete jobs?(yes/no)")
	if decision == "yes":
	        for job in f.readlines():
			jname=job.rstrip()
#	jname="z_mingjunl_test123123"
		        cmd=url+jname+"/doDelete\""
		        print "Deleting job:"+jname
	        	subprocess.call(cmd,shell=True)
	else :
		print "Give Up Delete Operation"
	

def Stop_last():
	for job in f.readlines():
		jname=job.rstrip()
#		jname="z_mingjunl_test"
		nextBuildNumber=open("/proj/hudson01/webhome/jobs/"+jname+"/nextBuildNumber","r")
		lastBuildNumber=int(nextBuildNumber.readline().rstrip())-1
		if lastBuildNumber>=1:
			print "The last build number is :",lastBuildNumber
			cmd = url+jname+"/"+str(lastBuildNumber)+"/stop\""
			print "stop the last build of "+jname
			subprocess.call(cmd,shell=True)
		else:
			print "Have not built before"


def Workspace():
	for job in f.readlines():
		jname=job.rstrip()
#		jname="z_mingjunl_test"
        	cmd=url+jname+"/doWipeOutWorkspace\""
	        print "wiping out workspace of "+jname
	        subprocess.call(cmd,shell=True)

def Rebuild_last():
	for job in f.readlines():
		jname=job.rstrip()
	        nextBuildNumber=open("/proj/hudson01/webhome/jobs/"+jname+"/nextBuildNumber","r")
                lastBuildNumber=int(nextBuildNumber.readline().rstrip())-1
		flag=Building(jname)
		if flag==0:
			print jname," is Disabled"
			continue
		elif flag==1:
			print jname," is building"
			continue
		else:
	                if lastBuildNumber>=1:
        	                print "The last build number is :",lastBuildNumber
                	        cmd = url+jname+"/"+str(lastBuildNumber)+"/rebuild/\""
	                        print "rebuild #"+str(lastBuildNumber)+" of "+jname
        	                subprocess.call(cmd,shell=True)
                	else:
                        	print "Have not built before"

def Rename():
	with open("old_name","r") as old:
		with open("new_name","r") as new:
			old_name=old.readlines()
			new_name=new.readlines()
			for oname,nname in zip(old_name,new_name):
				oname=oname.strip()
				nname=nname.strip()
				print "job name :",oname
				print "new job name:", nname
				url="\"https://"+user+":"+pwd+"@jenkins.mot.com/job/"+oname
				cmd="curl -k -d \"newName="+nname+"\" "+url+"/doRename\""
				print cmd
				subprocess.call(cmd,shell=True)



print "###################################"
print "    select opreation"
print "###################################"
print "1:Build_now"
print "2:Delete"
print "3:Stop Last Build"
print "4:Wipe Workspace"
print "5:Rebuild The Last"
print "6:Rename"
print "0:Quit"



n=int (raw_input("choice a selection : "))
options ={ 1: Build_now,
           2: Delete,
           3: Stop_last,
	   4: Workspace,
	   5: Rebuild_last,
	   6: Rename,
}

while n is not 0:
	options[n]()
	n=int (raw_input("choice a selection : "))
