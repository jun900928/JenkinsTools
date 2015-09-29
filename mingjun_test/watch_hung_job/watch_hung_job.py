"""
This tools is base on teams other tool
It will filter the jobs name from the output of other tools
And send the email to make a nitice
"""

import re
import os
import subprocess
import smtplib
from email.mime.text import MIMEText


def checking():
	print "###########start checking###########\n"
	os.system('/apps/tools/scm_tools/hudson_tools/hudson_job_monitor.pl -task hung > checking_output')
	print "----------checking is done----------"

def parsing():
	print '###########parising checkout###########\n'
	with open("checking_output","r") as f:
		data =f.readlines()
		count=0
		for line in data:
			if line.startswith("#"):
				break
			count+=1
	os.system('sed -i \'1,'+str(count)+'d\' checking_output')
	print '----------parsing is done----------'

def filtering():
	print "###########start filtering###########\n"
	jobs=[]
	with open("checking_output","r") as f:
	        p=re.compile('={10,}\n'
          	           '(\S.*?)'
                	     'Build.*?',re.DOTALL)
        	for m in p.finditer(f.read()):
			jobs.append(m.group(1).rstrip())
	print "----------end filtering----------"
	if len(jobs)<=2:
		print "the amount of hunging jobs is less than 3"
		print "will not send the e-mail"
		for item in jobs:
			print item
		return []
	return jobs

def send_email(jobs):
	if not jobs:
		return 
        content=""" """
        sender = ['mingjunl@motorola.com']
        receivers = ['mingjunl@motorola.com']
        for job in jobs:
                content=content+"""<a href='https://jenkins.mot.com/job/"""+job+"""'>"""+job+"""</a><br>"""
        message = MIMEText(content,_subtype='html',_charset='utf-8')
        message['Subject'] = "These Jobs Running More Than 4 hours"
        message['From'] = "From Mingjun <mingjunl@motorola.com>"
        message['To'] = "To Mingjun <mingjunl@motorola.com>"
        try:
                smtpObj = smtplib.SMTP('This part should be the SMTP server')
                smtpObj.sendmail(sender, receivers, message.as_string())
                print "Successfully sent email"
        except SMTPException:
                print "Error: unable to send email"


if __name__=="__main__":
	checking()
	parsing()
	jobs=filtering()
	send_email(jobs)
	
