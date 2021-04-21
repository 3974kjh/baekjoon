N = int(input())
def pibonaci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return (pibonaci(i-1) + pibonaci(i-2))
print(pibonaci(N))