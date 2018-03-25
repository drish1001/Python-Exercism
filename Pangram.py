ar = raw_input()
ar = ar.lower()
cnt =0
check = 'abcdefghijklmnopqrstuvwxyz'
for char in check:
    if ar.count(char)>0:
        cnt = cnt+1
if cnt==26:
    print("It is a pangram")
else:
    print("It is not a pangram")
