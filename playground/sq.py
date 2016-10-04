def Sq(x,n):
	if n == 0:
		return 0
	return Sq(x, n-1) + x
print(Sq(2,2))