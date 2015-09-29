import urllib2
import urllib


with urllib.urlopen("http://www.google.com") as a:
	print a.getcode()
	print a.readline()
	print a.info()
	print a.geturl()
#	jenkins=urllib.urlretrieve

