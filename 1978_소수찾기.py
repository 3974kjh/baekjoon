N = int(input())
k = map(int, input().split())
sosu = [2,3]
for i in range(3,1000,2):
    if i % 2 == 0 or i % 3 == 0:
        continue
    idx = 1
    cnt = 0
    while idx*idx <= i:
        if i % idx == 0:
            cnt+=1
        idx+=2
    if cnt == 1:
        sosu.append(i)
count = 0
for i in k:
    if i in sosu:
        count+=1
print(count)