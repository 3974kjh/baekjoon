N = list(map(str, input()))
idx = 0
for k in range(26):
    flag = 0
    for i in range(len(N)):
        if ord(N[i]) == k + 97:
            print(i, end=' ')
            flag = 1
            break
    if flag == 0:
        print(-1, end=' ')