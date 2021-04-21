sic = list(map(str, input()))
idx = 0
for i in sic:
    if i == '-':
        break
    idx+=1
res = sic[idx+1:]
here = []
plus = sic[:idx]
minus = []
plus_here = []
for i in range(len(res)):
    if res[i] == '-' or res[i] == '+' or i == len(res) - 1:
        if i == len(res) - 1:
            here.append(res[i])
        a = "".join(here)
        minus.append(a)
        here.clear()
    else:
        here.append(res[i])

for i in range(len(plus)):
    if plus[i] == '+' or i == len(plus) - 1:
        if i == len(plus) - 1:
            here.append(plus[i])
        b = "".join(here)
        plus_here.append(b)
        here.clear()
    else:
        here.append(plus[i])
plus_here = list(map(int, plus_here))
minus = list(map(int, minus))
A = sum(plus_here)
B = sum(minus)
print(A-B)