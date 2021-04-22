import sys
N = int(input())
p_num = [0] * 4001
m_num = [0] * 4001
num = []
for i in range(N):
    a = int(sys.stdin.readline())
    num.append(a)
    if a >= 0:
        p_num[a]+=1
    else:
        m_num[abs(a)]+=1
num.sort()
mean = sum(num) / N
here = []
p = max(p_num)
m = max(m_num)
for i in range(4001):
    if m_num[i] > 0:
        here.append((m_num[i],-i))
    if p_num[i] > 0:
        here.append((p_num[i],i))
cnt = 0
chebin = []
if p > m:
    bin = p
else:
    bin = m
print(round(mean))
print(num[N//2])
for x,y in here:
    if x == bin:
        cnt+=1
        chebin.append(y)
if cnt == 1:
    print(chebin[0])
else:
    chebin.sort()
    print(chebin[1])
print(max(num)-min(num))