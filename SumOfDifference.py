x=input("Enter the limit: ")
cnt=1
sum1=0
sum2=0
while cnt<=x:
	sum1=sum1+cnt
	cnt=cnt+1
print(sum1)
sum1=sum1*sum1
print(sum1)
cnt=1
while cnt<=x:
	sum2=sum2+(cnt*cnt)
	cnt=cnt+1
z=sum1-sum2
print(z)
