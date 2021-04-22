N = int(input())
here = [[]*1 for _ in range(201)]
for i in range(N):
    age, name = input().split()
    here[int(age)].append(name)
idx = 0
for i in here:
    for k in range(len(i)):
        print(idx, i[k])
    idx+=1