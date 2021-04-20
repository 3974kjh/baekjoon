import math
T = int(input())
for test in range(T):
    x, y = map(int, input().split())
    year = y - x
    if year > 3:
        k = int(math.sqrt(year))
        here = year - k*k
        start = k + k - 1
        if here == 0:
            print(start)
        else:
            if here % k == 0:
                here-=1
            plus = (here // k) + 1
            print(start+plus)
    else:
        print(year)