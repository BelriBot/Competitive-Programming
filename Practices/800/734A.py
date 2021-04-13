




#py 3.8 solution
#n = int(input())
#s = input()
#print("Anton" if(a:= s.count("A"))>(b:=n-a)else "Danik" if a<b else "Friendship")



n=int(input())
s=[*map(str,input().strip())]
c=0
for i in s:
    if i == "A":
        c+=1        
if len(s)-c > c:
    print("Danik")
elif len(s)-c < c:
    print("Anton")
else:
    print("Friendship")
    
