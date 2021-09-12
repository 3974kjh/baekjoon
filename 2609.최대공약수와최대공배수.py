A, B = list(map(int, input().split()))

k = 2
here = []
while (1):
    if (A % k == 0 and B % k == 0):
        A = A // k
        B = B // k
        here.append(k)
    else:
        k+=1
        if (k > A or k > B):
            break
res = 1
for i in range(len(here)):
    res = res * here[i]
print(res)
print(res * A * B)