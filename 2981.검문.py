N = int(input())
M = []
new1=[]
new2=[]
newcheck=[]
for i in range(N):
    M.append(int(input()))
for i in range(N-1):
    a = abs(M[i] - M[i+1])
    num = 1
    while (int(a**0.5) >= num):
        if (a % num == 0):
            if num != 1 and num != a // num:
                new1.append(num)
            new1.append(a // num)
        num+=1
    for p in range(len(new1)):
        for q in range(len(new2)):
            if (new1[p] == new2[q]):
                newcheck.append(new1[p])
    if (i >= 1):
        new1 = newcheck.copy()
        newcheck.clear()
    new2 = new1.copy()
    new1.clear()
new2.sort()
for i in range(len(new2)-1):
    print(new2[i],end = " ")
print(new2[len(new2)-1], end='')