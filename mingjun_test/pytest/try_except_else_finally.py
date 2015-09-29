
def a():
	try:
		print 'try'
		raise "invalid"
		print "after raise"
#		return
	except:
		print 'except'
		return
	else:
		print 'else'
		return
	finally:
		print 'finally'
		return 

a()
