import urllib2

url="https://mingjunl:LMJ900928mg~@jenkins.mot.com/job/z_mingjunl_test2/api/xml"


files={"file":open("config.xml")}
headers={'Content-Type': 'application/xml'}
with open("config.xml","r") as f:
	data=f.read()
	req=urllib2.Request(url,data,headers)
	urllib2.urlopen(req)


