def permutation(n,a):
	r=[]
	for item in a:
		for i in range(len(item)):
			temp=item[:]
			temp.insert(i,n)
			print temp
			r.append(temp)
		temp=item[:]
                temp.append(n)
		r.append(temp)
		print temp
	return r


n=3
result=[[0]]
for i in range(1,n):
	result=permutation(i,result)
print result
