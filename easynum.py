N = int(input())
here = [0 for i in range(10)]
hi = []
def check(i, N):
    global hi
    hi = [i]
    num = 1
    dell = 1
    while(N > num):
        ll = len(hi)
        cnt = -1
        for k in range(ll):
            if (hi[k]-1 != -1):
                hi.append(hi[k]-1)
            if (hi[k]+1 != 10):
                hi.append(hi[k]+1)
        for idx in range(1, dell+1):
            hi[idx-1],hi[len(hi)-idx] = hi[len(hi)-idx],hi[idx-1]
        for _ in range(1, dell+1):
            hi.pop()
        num+=1
        dell = len(hi)
    here[i] = len(hi)
    hi.clear()

for i in range(1, 10):
    check(i, N)
print(sum(here) % 1000000000)