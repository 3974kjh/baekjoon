T = int(input())
for test in range(T):
    N = int(input())
    here = [(1,0),(0,1)]
    for i in range(N+1):
        if i > 1:
            a, b = here[i-2]
            x, y = here[i-1]
            here.append((a+x,b+y))
    res = here[N]
    print(res[0], res[1])