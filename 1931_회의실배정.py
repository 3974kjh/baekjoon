N = int(input())
here = []
for i in range(N):
    s,e = map(int,input().split())
    here.append((s,e))
here.sort(key=lambda a: a[0])
here.sort(key=lambda a: a[1])
a, b = here[0]
cnt = 1
for i in range(1, len(here)):
    x, y = here[i]
    if b <= x:
        b = y
        cnt+=1
print(cnt)