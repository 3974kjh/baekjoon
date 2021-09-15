n = int(input())
res = []
stack = []
check = []
idx = 0
for i in range(n):
    res.append(int(input()))
for i in range(1,len(res)+1):
    stack.append(i)
    check.append('+')

    for j in range(len(stack)):
        if stack[len(stack)-1] == res[idx]:
            stack.pop()
            check.append('-')
            idx+=1
        else:
            break
if (len(stack) != 0):
    print('NO')
else:
    for out in check:
        print(out)
    