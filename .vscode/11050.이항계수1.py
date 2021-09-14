N, K = map(int, input().split())
res1 = 1
res2 = 1
cnt = 1
if K == 0:
    print(1)
else:
    for i in range(N,0,-1):
        res1 = res1 * i
        if cnt == K:
            break
        cnt+=1
    for i in range(K,0,-1):
        res2 = res2 * i
    print(res1//res2)