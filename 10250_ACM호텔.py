T = int(input())
for test in range(T):
    H,W,N = map(int, input().split())
    if N % H == 0:
        w = (N // H) - 1
    else:
        w = N//H 
    h = N - w*H
    print(h,end='')
    if w < 9:
        print('0',end='')
        print(w+1)
    else:
        print(w+1)