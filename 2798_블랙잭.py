N,M = map(int, input().split())
num = list(map(int, input().split()))
here = []
for i in range(len(num)):
    for j in range(i+1, len(num)):
        for k in range(j+1, len(num)):
            if num[i] + num[j] + num[k] <= M:
                here.append(num[i]+num[j]+num[k])
print(max(here))