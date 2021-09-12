while (1):
    A, B = list(map(int, input().split()))
    if (A == 0 and B == 0):
        break
    elif A == 0 or B == 0:
        print("neither")
    elif (B % A == 0 ):
        print("factor")
    elif (A % B == 0):
        print("multiple")
    else:
        print("neither")

