x=raw_input("Enter the number: ")
key=input("Enter the key: ")
cnt=0
l=len(x)
e=key
mx=0
b=0
while (e<=l):
	z=x[b:e]
	temp=z
	pro=1
	for char in temp:
		a=ord(char)-48
		pro=pro*a
	b=b+1
	e=e+1
	if mx<pro:
		mx=pro
print(pro)
	
	
	
