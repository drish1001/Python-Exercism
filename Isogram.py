a = str(input())
c=0
if a=="":
    print("Not an isogram")
else :
    for char in a:
        if a.count(char)>1:
            c=c+1
        else:
            c=c
if c>0:
    print ("Not an isogram")
else:
    print ("Isogram")
