import collections

l=[1,
  [2,2.1,2.2],
   3]


def lam(list):
	for num in list:
		print num
		if isinstance(num,collections.Iterable):
			lam(num)


lam(l)
		
