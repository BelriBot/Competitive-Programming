n=input()
c=0
for i in n:
    if i in ["4","7"]:
        c+=1
if c in [4,7]:
    print("YES")
else:
    print("NO")
