M = int(input())
N = int(input())

sosu = [2,3]
for i in range(3,10000,2):
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
here = []
for i in sosu:
    if i < M:
        continue
    if i > N:
        break 
    if i >= M:
        here.append(i)
if len(here) == 0:
    print(-1)
else:   
    print(sum(here))
    print(min(here))