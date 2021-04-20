N = int(input())
alpha = []
res = 0
for i in range(N):
    k = input()
    alpha.append(k)
for a in alpha:
    check = [[0]*1 for _ in range(26)]
    idx = 0
    here = ord(a[0]) - 97
    check[here].append(1)
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            here = ord(a[i+1]) - 97
            check[here][0]+=1
        else:
            here = ord(a[i+1]) - 97
            check[here].append(1)
    flag = 0
    for i in check:
        if len(i) > 2:
            flag = 1
    if flag == 0:
        res+=1
print(res)