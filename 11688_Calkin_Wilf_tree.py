T = int(input())
for test in range(T):
    a, b = 1, 1
    tree = list(map(str, input()))
    for i in tree:
        if i == 'L':
            b+=a
        elif i == 'R':
            a+=b
    print(f"#{test+1} {a} {b}")