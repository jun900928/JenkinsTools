Str="adxzgsadgsadgfsASF"
l= list(Str)
print Str
print l
for i in range(1,(len(Str)-1)/2):
	l[i],l[-i-1]=l[-i-1],l[i]

print l
s="".join(l)
print s
	

