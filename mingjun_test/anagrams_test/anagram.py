l=["dream","made","stop","armed","dame","pots","mead","post"]
l_s=[]
output=[]
for item in l:
	new="".join(sorted(item))
	l_s.append(new)
	
for item in l_s:
	print l[l_s.index(item)]
	output.append(l[l_s.index(item)])
	l.remove(l[l_s.index(item)])
	l_s.remove(item)
	while item in l_s:
		print l[l_s.index(item)]
		output.append(l[l_s.index(item)])
	        l.remove(l[l_s.index(item)])
	        l_s.remove(item)

print output
