X = int(input())
cnt = 0

def three(x):
    global X
    global cnt
    a = 3
    c = 0
    X = X - x
    while (X >= a):
        a = a * 3
        c+=1
    if X == a // 3:
        cnt = cnt + c + x
        return(1)
    else:
        X = X + x
        return(0)
    
while (X != 1):
    if ((X-1)%3==0 or (X-2)%3==0):
        if (X-1)%3==0 and three(1):
            break
        elif three(2):
            break
    if (X % 3 == 0):
        X = X // 3
        cnt+=1
    elif (X % 2 == 0):
        X = X // 2
        cnt+=1
    else:
        X-=1
        cnt+=1
print(cnt)