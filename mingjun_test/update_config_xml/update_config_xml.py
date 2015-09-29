"""
This tool is to update the configure.xml"

"""

import xml.etree.ElementTree as ET
import os
import getpass
import subprocess
import requests


jobs_name="jobs_name.txt"
path ="/proj/hudson01/webhome/jobs/"
url1="curl -k -X POST -d @config.xml https://"
url2="@jenkins.mot.com/job/"
url3="/config.xml --header \"Content-Type:text/xml\""


def edit_xml(job):
	xml_file=path+job+"/config.xml"
	tree=ET.parse(xml_file)
	root=tree.getroot()
#	for item in root.getiterator("command"):
#		print item.text

############## This part is the target need to find ##################
	target=root.find("builders")
#	target=root.find("publishers")

########################## END HERE ##################################

	s=target[0][0].text

############## This part is the repalce strings ######################
	s1="-manifest_url=ssh://gerrit.mot.com:29418/home/repo/dev/platform/android/platform/manifest.git"
	s2="-manifest_url=ssh://gerrit.mot.com:29418/home/repo/dev/platform/android/platform/manifest/m.git"
######################## END HERE ####################################
	s=s.replace(s1,s2)
	target[0][0].text=s
#save the xml in the current directory
	tree.write("config.xml")

#use curl commands
def post_xml(name,pwd,job):
	with open ("config.xml","rb") as data:
		url="https://"+name+":"+pwd+"@jenkins.mot.com/job/"+job+"/config.xml"
		p = subprocess.Popen(["curl", "-k", "-X", "POST", "-d",data.read(),url], stdout=subprocess.PIPE)
		out, err = p.communicate()
		print job.rstrip()," is done"

"""
#use requests function
def post_xml(name,pwd,job):
	auth = requests.auth.HTTPBasicAuth(name, pwd)
	request_args = {
                        'allow_redirects' : True,
                        'auth'            : auth,
                        'verify'          : False,
                       }
	url='https://jenkins.mot.com/job/'+job+'/config.xml'
	headers = {'content-type': 'application/xml'}
	request = requests.post(url,open('config.xml','rb'), **request_args)
	print request
        if '200' in str(request):
		print "+++++++++++++++++++++++++++++++++++++++++++++++"
		print job.rstrip()," is done"
		print "+++++++++++++++++++++++++++++++++++++++++++++++"
        else:
                print "failed"

"""


if __name__ == "__main__":
	name=raw_input("user name: ")
	pwd=getpass.getpass("password: ")
	with open(jobs_name,"r") as f:
		for job in f.readlines():
			edit_xml(job.rstrip())
			post_xml(name,pwd,job.rstrip())
