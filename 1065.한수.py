N = int(input())
cnt = 0
for i in range(1, N+1):
    if i < 100:
        cnt+=1
    else:
        k = str(i)
        chai = int(k[1]) - int(k[0])
        ok = 1
        for j in range(1,len(k)-1):
            if chai == int(k[j+1]) - int(k[j]):
                ok+=1
        if len(k) - 1 == ok:
            cnt+=1
        ok = 1
print(cnt)