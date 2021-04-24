N = int(input())
a = str(666)
cnt = 0
while 1:
    if '666' in a:
        cnt+=1
        if cnt == N:
            print(a)
            break
    a = int(a) + 1
    a = str(a)