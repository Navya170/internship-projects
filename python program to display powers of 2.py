# PYTHON PROGRAM TO DISPLAY POWERS OF 2 


terms=10
result=list(map(lambda x:2**x,range(terms)))
print("the total terms are:",terms)
for i in range(terms):
	print("2^",i,"=",result[i])
