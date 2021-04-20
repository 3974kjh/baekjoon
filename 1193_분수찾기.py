N = int(input())
i = 0
while 1:
    if (i * (i+1)) // 2 >= N:
        break
    else:
        i+=1
end = (i * (i+1)) // 2
where = end - N
if i % 2 == 1:
    if where == 0:
        print(1,end='')
        print('/',end='')
        print(i)
    else: 
        print(where+1,end='')
        print('/',end='')
        print(i-where)
else:
    if where == 0:
        print(i,end='')
        print('/',end='')
        print(1)
    else: 
        print(i-where,end='')
        print('/',end='')
        print(where+1)