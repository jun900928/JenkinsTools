class parent:
	x=5

class child1(parent):
	pass

class child2(parent):
	pass

print parent.x,child1.x,child2.x

child1.x=2

print parent.x,child1.x,child2.x

parent.x=6

print parent.x,child1.x,child2.x
