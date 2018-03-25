y= int(input())
if (y%4==0):
    if ((y>1000) and (y%400==0)):
        print("leap year")
    else:
        print("Not A Leap Year")
else:
    print ("Not a lep year")
