n=int(input("enter a number:"))
sum=0
temp=n
a=len(str(n))
while n>0:
	r=n%10
	sum=r**a+sum
	n=n/10
if temp==sum:
	print("it is armstrong number")
else:
	print("it is not a armstrong number")

