N = int(input())
here = []
i = 2
while N > 1:
    if N % i == 0:
        here.append(i)
        N = N // i
    else:
        i+=1
for i in here:
    print(i)