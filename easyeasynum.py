T = int(input())

num = [[0]*12 for _ in range(100)]
idx = 1
N = T
for i in range(1,11):
    num[0][i] = 1
while (T-1):
    for i in range(1, 11):
        num[idx][i] = num[idx-1][i-1] + num[idx-1][i+1]
    T-=1
    idx+=1
print(sum(num[N-1][1:10]) % 1000000000)