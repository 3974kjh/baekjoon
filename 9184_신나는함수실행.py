def w(a,b,c):
    if dp[a+50][b+50][c+50] != 0:
        return dp[a+50][b+50][c+50]
    if a <= 0 or b <= 0 or c <= 0:
        dp[a+50][b+50][c+50] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        here = w(20, 20, 20)
        dp[a+50][b+50][c+50] = here
        return here
    elif a < b and b < c:
        here = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        dp[a+50][b+50][c+50] = here
        return here
    else:
        here = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        dp[a+50][b+50][c+50] = here
        return here
res = []
arr = []
dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
while 1:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    arr.append((a, b, c))
    res.append(w(a,b,c))
for i in range(len(res)):
    print(f'w{arr[i]} = {res[i]}')