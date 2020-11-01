def  squirrel(n):
	if n ==0:
		return 1
	return int(str(abs(squirrel(n-1) * n))[0])
print (squirrel(5))