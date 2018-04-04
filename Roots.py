import math
a=input('enter a -')
b=input('enter b-')
c=input('enter c-')
d=b*b-4*a*c
if d>0:
  r1=(-b+math.sqrt(d))/(2.0*a)
  r2=(b+math.sqrt(d))/(2.0*a)
  print 'roots are real and unequal'
  print r1 and r2
elif d==0:
    print'roots are real and equal'
else:
      print'roots are imaginary'
