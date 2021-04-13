
s=str(input())
c=0
for i in s:
    if i.isupper():
        c+=1
r=len(s)
if r-c < c:
    print(s.upper())
else:
    print(s.lower())





