N = int(input())
here = []
for i in range(N):
    x,y = map(int,input().split())
    here.append((x,y))
here.sort()
for i, j in here:
    print(i, j)