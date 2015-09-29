"""
This tool is to remove the upstream jobs in configuration
Automaticly remove "Build after other projects are built"

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
	target=root.find("triggers")
	for child in target:
		target.remove(child)
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
        name=raw_input("username :")
        pwd=getpass.getpass("password :")
        d={'@':'%40','&':'%26'}
        for i,j in d.iteritems():
                pwd=pwd.replace(i,j)
        if checkpwd(username,pwd) is not 200:
                print "wrong username or password"
                sys.exit()
        else:
                print "Username and Password is good.................."

	with open(jobs_name,"r") as f:
		for job in f.readlines():
			edit_xml(job.rstrip())
			post_xml(name,pwd,job.rstrip())
