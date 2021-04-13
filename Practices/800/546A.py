
k,n,w=map(int,input().split())
#cost of first banana
#total amount of dollars the soldier as acquired
#total number of bananas the solider wants to acquire
c=0
t=k*w
if n>t:
    c=n-t
    n=n-c

print(n)
    
