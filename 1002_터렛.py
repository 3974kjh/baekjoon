import math
T = int(input())
for test in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    R = math.sqrt(abs(x_1 - x_2)**2 + abs(y_1 - y_2)**2)
    here = [R, r_1, r_2]
    here.sort()
    if R == 0 and r_1 == r_2:
        print(-1)
    elif here[2] > here[0] + here[1]:
        print(0)
    elif r_2 == R + r_1:
        print(1)
    elif R == r_1 + r_2:
        print(1)
    elif r_1 == R + r_2:
        print(1)
    else:
        print(2)