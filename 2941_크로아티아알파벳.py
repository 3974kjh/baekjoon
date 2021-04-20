N = input()
croatina = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for k in range(len(N)-1):
    two_check = "".join(N[k:k+2])
    for i in range(len(croatina)):
        if croatina[i] in two_check:
            cnt+=1
for k in range(len(N)-2):
    three_check = "".join(N[k:k+3])
    if 'dz=' in three_check:
        cnt+=1
res = len(N) - cnt*2
res+=cnt
print(res)