x=int(input())
cnt=0
a=x
initial=x
while x>0:
	x=x/10
	cnt=cnt+1
print(cnt)
sum=0
while a>0:
	r=a%10
	sum=sum+(r^cnt)
	a=a/10
if initial==sum:
	print("It is an angstrom number")
else:
	print("Not an angstrom number")
	
