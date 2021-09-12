num = int(input())

N  = list(map(int, input().split()))
N.sort()
print(N[0] * N[len(N)-1])