l=input("Enter the limit: ")
x=raw_input("Enter the multiples: ")
sum=0
for char in x:
	a=ord(char)
	if(a>48)and(a<=57):
		d=a-48
		while(sum<=l):
			sum=sum+d
		
			print(sum)
	if(a==32):
		print("LOL")
print(sum)
