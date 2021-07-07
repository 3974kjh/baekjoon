N = int(input())
tri = []
for i in range(N):
    k = list(map(int, input().split()))
    tri.append(k)
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            tri[i][j] = tri[i-1][j] + tri[i][j]
        elif j == i:
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
        else:
            tri[i][j] = max(tri[i-1][j] + tri[i][j], tri[i-1][j-1] + tri[i][j])
print(max(tri[N-1]))