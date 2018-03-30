x=raw_input("Enter the code: ")
for char in x:
	a=ord(char)
	if (a>=65)and(a<=90):
		a=155-a
		char=chr(a)
	if (a>=97)and(a<=122):
		a=219-a
		char=chr(a)
	print(char)
