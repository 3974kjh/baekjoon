N = int(input())
here = []
for i in range(N):
    here.append(input())
idx = 0
here.sort()
for i in range(N-1):
    if here[idx] == here[idx+1]:
        del(here[idx+1])
    else:
        idx+=1
here_len = [[]*1 for _ in range(51)]
for i in range(len(here)):
    here_len[len(here[i])].append(here[i])
for i in here_len:
    i.sort()
    for k in range(len(i)):
        print(i[k])