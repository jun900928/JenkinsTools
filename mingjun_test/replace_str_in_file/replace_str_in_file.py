"""
Test tool
Try to replace some word in the same file by read() and write()

"""

import urllib

#print urllib.urlopen("http://www.google.com").read().decode("big5").encode("utf8")


with open("1.txt","r") as f1:
#f2=open("1.txt","w")
	data = f1.readlines()
	data2=[]
	for line in data:
		line=line.replace("1","a")
		data2.append(line)

with open("1.txt","w") as f2:
	for line in data2:
		print line.rstrip()
	f2.writelines(data2)
