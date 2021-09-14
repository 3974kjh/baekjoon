N = int(input())
line = list(map(int, input().split()))
cost = list(map(int, input().split()))
k = cost[0]
res = k * line[0]
for i in range(1,len(line)):
    if (k > cost[i]):
        k = cost[i]
    res+=k * line[i]
print(res)