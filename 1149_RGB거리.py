N = int(input())
index = []
for i in range(N):
    index.append(list(map(int, input().split())))
for i in range(1, N):
    index[i][0] = min(index[i-1][1], index[i-1][2]) + index[i][0]
    index[i][1] = min(index[i-1][0], index[i-1][2]) + index[i][1]
    index[i][2] = min(index[i-1][0], index[i-1][1]) + index[i][2]
print(min(index[N-1]))