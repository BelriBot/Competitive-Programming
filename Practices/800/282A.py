
n = int(input())
s = 0
while n >= 1:
     p = str(input())
     n = n-1
     if "++" in p:
        s += 1
     elif "--" in p:
        s -= 1
print(s)
    
