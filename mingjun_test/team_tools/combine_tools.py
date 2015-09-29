"""
This tool combines the whole  team's tools
And generatet the command as need 
"""

import subprocess

print "##################################################################"
print "this is for generate tools command\n"
print "##################################################################"
print "1:add_permissions_for_user_to_job.pl"
print "2:archive_one_job_from_jenkins.pl"
print "3:clone_a_job"
print "4:enable_or_disable_jobs"

fname="job_list.txt"
output='command'
old_name_file='old_name.txt'
new_name_file='new_name.txt'
def add_permission():
	s="/apps/tools/scm_tools/hudson_tools/Jenkins_config/add_permissions_for_user_to_job.pl "
        c1='-job_build '
	c2='-job_cancel '
	c3='-job_read '
	c4='-user '
	print 'input coreid'
	c5=raw_input()
	f=open(fname,'r')
	f2=open(output,'w')
	for line in f.readlines():
#		print line
		f2.write(s+c1+c2+c3+c4+c5+' '+line)
		print s+c1+c2+c3+c4+c5+' '+line.rstrip()
 	f.close()
	f2.close()
	print 'output file is :',output
		
		

def archive():
        s="/apps/tools/scm_tools/hudson_tools/Jenkins_config/archive_one_job_from_jenkins.pl "
        f=open(fname,'r')
	f2=open(output,'w')
        for line in f.readlines():
                print s+line.rstrip() 
		f2.write(s+line)
        f.close()
	f2.close()
	print 'output file is :',output	

def clone():
	s='/apps/tools/scm_tools/hudson_tools/Jenkins_config/clone_a_job.pl -old_job='
	c1=' -new_job='
	c2=' -manifest_branch=mlmp-stable2-thea-p2'
	c3=' -tag_info_prefix=LXB22.99-24-Thea'
	c4=' -job_description description.txt'
	f=open(old_name_file,'r')
        f1=open(new_name_file,'r')
        f2=open(output,'w')
        for line,line1 in zip(f.readlines(),f1.readlines()):
                print s+line.rstrip()+c1+line1.rstrip()+c2+c3+c4
                f2.write(s+line.rstrip()+c1+line1.rstrip()+c2+c3+c4+'\n')
        f.close()
	f1.close()
        f2.close()
	print 'output file is :',output

def enable_or_disable():
        s="/apps/tools/scm_tools/hudson_tools/Jenkins_config/enable_or_disable_jobs.pl "
	c1=' -disable '
        f=open(fname,'r')
        f2=open(output,'w')
        for line in f.readlines():
                print s+c1+line.rstrip()
                f2.write(s+c1+line)
        f.close()
        f2.close()
	print 'output file is :',output

n=int (raw_input())
options ={ 1: add_permission,
	   2: archive,
           3: clone,
           4: enable_or_disable,
}

options[n]()

subprocess.call(["chmod",'+x',output])
