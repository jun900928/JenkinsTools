import requests

status =0
while status !=200:
	try:
	    r = requests.head("https://mingjun:LMJ@jenkins.mot.com/")
	    status=int(r.status_code)
	    #prints the int of the status code
	    if status != 200:
		print "There are some problem with your username or password "
		print "If you want to quit, press Ctrl+C"
		pwd=
	    else:
		print "-----your username and password pass--------/n" 
	except requests.ConnectionError:
	    print("failed to connect")
