"""
This tool is to replace a word in the file.
It uses the "sed" command to edit file
"""

import subprocess

print "input file name"
file_name=raw_input()
print "orginal word"
o=raw_input()
print "replace world"
r=raw_input()
cmd="s/"+o+"/"+r+"/g"
subprocess.call(["sed", "-i", cmd, file_name])
print "file name:",file_name


#p = subprocess.Popen(["sed","-i","s/111/bar/g","1.txt"], stdout=subprocess.PIPE)output, err = p.communicate()
