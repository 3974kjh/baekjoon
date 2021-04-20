N = list(map(str, input()))
for i in range(len(N)):
    if 97 <= ord(N[i]) <= 122:
        k = ord(N[i]) - 32
        N[i] = chr(k)
check = [0]*26
for i in range(26):
    for n in N:
        if i + 65 == ord(n):
            check[i]+=1
res = max(check)
cnt = 0
here = 0
for idx in range(26):
    if res == check[idx]:
        here = idx
        cnt+=1
if cnt > 1:
    print('?')
else:
    print(chr(here+65))