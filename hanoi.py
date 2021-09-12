N = int(input())

def hanoi(N, a,b,c):
    if N == 0:
        return
    else:
        hanoi(N-1, a, c, b)
        print(a, c)
        hanoi(N-1, b, a, c)
print(2**N - 1)
hanoi(N,1,2,3)