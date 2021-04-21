while 1:
    x,y,z = map(int,input().split())
    if x == 0 and y == 0 and z == 0:
        break
    if z**2 == x**2 + y**2:
        print('right')
    elif x**2 == y**2 + z**2:
        print('right')
    elif y**2 == x**2 + z**2:
        print('right')
    else:
        print('wrong')