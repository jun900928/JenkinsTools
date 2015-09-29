#####################################################
## This tool is to filter the paramaters form job ##
## It can print the job name and the whole line of #
## the parameters.                                 #
#####################################################
import subprocess

f="job_list.txt"
path="/proj/hudson01/webhome/jobs/"
rep={'-':'\-','_':'\_'}

keyword_1=raw_input("input keywords(eg:-product_group): ")
flag=raw_input("do you need to output the job name(y/n)?:")

def replace_all(text,dic):
	for i,j in dic.iteritems():
		text=text.replace(i,j)
	return text


keyword=replace_all(keyword_1,rep)
#print keyword+"\n"

with open(f,"r") as jobs:
	for job in jobs.readlines():
		f_name=path+job.rstrip()+"/config.xml"
		if flag=="y":
			print "job name is:",job.rstrip()
		p = subprocess.Popen(['grep',keyword,path+job.rstrip()+"/config.xml"], stdout=subprocess.PIPE)
		output, err = p.communicate()
		re={"=":" ","\\":""}
		#if you do not need to print the keyword
		#output=output.replace(keyword_1,"")
		if not output:
			output="NULL\n"	
		print "output is:",replace_all(output,re)
