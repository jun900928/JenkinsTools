
class Base(object):
	def f1(self):
		print "base.f1"
	def f2(self):
		print "base.f2"
	def f3(self):
		print "base.f3"
class Base2(object):
	def f4(self):
		print "base2.f4"

class Base3(Base2):
	def f5(self):
		print "base3.f5"


"""
class Child(Base):
#multiple inerence
	def __init__(self):
		self.base2=Base2()
		self.base3=Base3()
	def f4(self):
		self.base2.f4()
	def f5(self):
		self.base3.f5()
"""
class Child(Base2,Base3):
#multiple inerence

#override
	def f1(self):	
		print "child.F1"
#super
	def f2(self):
		super(Child,self).f2()

#implict
	



c=Child()
b=Base()
b2=Base2()
b3=Base3()
print "***********multiple inherence**********"
print "I am Base2 (inherite from object)"
b2.f4()
print "I am Base3 (inherite form base2)"
b3.f4()
print "I am child:"
c.f4()
#c.f5()
print "******************override*************"
b.f1()
c.f1()
print"*******************super****************"
b.f2()
c.f2()
print "*****************implict***************"
b.f3()
c.f3()
