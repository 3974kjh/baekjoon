N = int(input())
stack = []
res = []
for i in range(N):
    a = input().split()
    if (a[0] == 'push'):
        stack.append(int(a[1]))
    elif (a[0] == 'pop'):
        if len(stack):
            res.append(stack.pop())
        else:
            res.append(-1)
    elif (a[0] == 'size'):
        res.append(len(stack))
    elif (a[0] == 'empty'):
        if len(stack):
            res.append(0)
        else:
            res.append(1)
    elif (a[0] == 'top'):
        if len(stack):
            res.append(int(stack[len(stack)-1]))
        else:
            res.append(-1)
for i in range(len(res)):
    print(res[i])