T = int(input())
for i in range(T):
    stack = input()
    res = 0
    for n in range(len(stack)):
        if stack[n] == '(':
            res+=1
        elif stack[n] ==')':
            res-=1
        if (res < 0):
           out = 'NO'
           break
    if (res == 0):
        out = 'YES'
    else:
        out = 'NO'
    print(out)