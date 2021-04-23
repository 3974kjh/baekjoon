N = int(input())
flag = 0
for i in range(1,N+1):
    num = list(map(int, str(i)))
    res = i + sum(num)
    if res == N:
        flag = 1
        print(i)
        break
if flag == 0:
    print(0)