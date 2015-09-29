
def divide(x,y):
	try:
#		print "before try return"
#		return "try"
		result =x/y
#		print "x/y= ",result
		print "last action before return"
#		return "big 0"
	except ZeroDivisionError:
		print "division by zero"
	except :
		print "other exception"
	else:
		print "this is else "
		return "else"
	finally:
		print "this is finally"
#		return "final"



print divide(3,1)
