num=input("Enter the limit: ")
x=2
cnt=0
while (x<=num):
	a=2
	while(a<=x):
		x%a==0
		cnt=cnt+1
		a=a+1
	if cnt==1:
		print(x)
	x=x+1
