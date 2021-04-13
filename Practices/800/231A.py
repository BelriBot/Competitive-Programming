
n=int(input())
success=0

for i in range(n):
    des=input().replace(" ", "")
    des1=int(des)
    if des1 >= 101:
        success = success + 1
    elif des1 == 11:
        success = success + 1
    else:
        success = success + 0

    n = n -1
    
print(success)


    
    
