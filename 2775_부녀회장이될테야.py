T = int(input())
for test in range(T):
    k = int(input())
    n = int(input())
    apart = [[0] * n for _ in range(k+1)]
    for i in range(n):
        apart[0][i] = i+1
    for i in range(k):
        for j in range(n):
            res = 0
            for z in range(j+1):
                res+=apart[i][z]
            apart[i+1][j] = res
    print(apart[k][n-1])