
n=int(input());p=str(input().split());c=0
for i in p:
    if i=="0":
        c+=1
if n-c==0:
    print("EASY")
else:
    print("HARD")



