M,N = map(int, input().split())
prime = [2] 
visited = [0]*1000001
for q in range(3,1000001,2):
    if visited[q] == 0:
        prime.append(q)
        for w in range(q,1000001,q):
            if w%q == 0:
                visited[w] = 1
here = []
for i in prime:
    if i < M:
        continue
    if i > N:
        break 
    if i >= M:
        here.append(i)
for i in here:
    print(i)