X = int(input())

minnum = [0,0,1,1,2]
for i in range(5, X+1):
    minnum.append(minnum[i-1] + 1)
    if (i % 3 == 0):
        minnum[i] = min(minnum[i//3] + 1, minnum[i])
    if (i % 2 == 0):
        minnum[i] = min(minnum[i//2] + 1, minnum[i])
print(minnum[X])