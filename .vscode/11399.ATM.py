N = int(input())
A = list(map(int, input().split()))
A.sort()
num = A[0]
res = [num]
for i in range(1,len(A)):
    num+=A[i]
    res.append(num)
print(sum(res)) 