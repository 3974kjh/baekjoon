T = int(input())
prime = [2] 
visited = [0]*10000
for q in range(3,10000,2):
    if visited[q] == 0:
        prime.append(q)
        for w in range(q,10000,q):
            if w%q == 0:
                visited[w] = 1
for test in range(T):
    n = int(input())
    half = n//2
    for j in range(half, 1, -1):
        if (n - j in prime) and (j in prime):
            print(j, n-j)
            break