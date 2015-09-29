import subprocess

url="https://mingjunl:LMJ900928mg~@jenkins.mot.com/job/z_mingjunl_test2/config.xml"

data=open("config.xml","r")
p = subprocess.Popen(["curl", "-k","-X","POST","-d",data.read(),url], stdout=subprocess.PIPE)
out, err = p.communicate()
print out
