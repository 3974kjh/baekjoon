import math

N = int(input())
if N > 7:
    A = (N-1) / 3
    math.ceil(A)
    if A > 100:
        i = 10
    elif A > 10000:
        i = 100
    elif A > 1000000:
        i = 1000
    elif A > 100000000:
        i = 10000
    else:
        i = 1
    while 1:
        if i * (i+1) >= A:
            print(i+1)
            break
        else:
            i+=1
else:
    if N == 1:
        print(1)
    else:
        print(2)