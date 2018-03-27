x=raw_input()
key=input("Enter the key: ")
for char in x:
	r=ord(char)
	r=r-key
	print(chr(r))

