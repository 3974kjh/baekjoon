N = int(input())
f_res = 0
t_res = 0
while N >= 0:
    if N % 5 == 0:
        f_res = N // 5
        break
    else:
        N-=3
        t_res+=1
if f_res == 0 and N % 3 != 0:
    print(-1)
else:
    res = f_res + t_res
    print(res)