prime = [2] 
visited = [0]*246913
for q in range(3,246913,2):
    if visited[q] == 0:
        prime.append(q)
        for w in range(q,246913,q):
            if w%q == 0:
                visited[w] = 1
while 1:
    n = int(input())
    if n == 0:
        break
    here = []
    for i in prime:
        if i <= n:
            continue
        if i > 2*n:
            break 
        if i > n:
            here.append(i)
    print(len(here))