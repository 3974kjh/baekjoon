T = int(input())
for test in range(T):
    N = list(map(str, input().split()))
    num = int(N[0])
    for i in N[1]:
        for j in range(num):
            print(i, end='')
    print('')