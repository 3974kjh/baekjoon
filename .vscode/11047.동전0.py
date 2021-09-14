N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))
cnt = 0
for i in range(len(coin)-1,-1,-1):
    a = 1
    num = coin[i]
    if (K >= num):
        a = K // num
        cnt+=a
        num = coin[i] * a
        K-=num
    if (K == 0):
        break
print(cnt)
