x=input()
y=10
print(y)
sum=0
z=1
while (z<=y):
    a=int(x%10)
    sum=sum+(a*z)
    x=x/10
    z=z+1
if (sum%11==0):
    print("ISBN digit")
else:
    print("Not an ISBN digit")
    
