""""
This tool is to filter the job names from the email Watchdog run for hung jobs

1.paste the email content into file "email" in the same folder
2.run this script
"""
import re

with open("email","r") as f:
#	print f.read()i
#	p=re.compile(r'Build')
	p=re.compile('={10,}\n'
		     '(\S.*?)'
		     'Build.*?',re.DOTALL)
#	p=re.compile(r'(=+)(.*?)(Build.)')
	for m in p.finditer(f.read()):
		print m.group(1).rstrip()
