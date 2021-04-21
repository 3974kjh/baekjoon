N = int(input())
def factorial(res,N):
    if N > 0:
        res*=N
        return factorial(res,N-1)
    print(res)
factorial(1,N)