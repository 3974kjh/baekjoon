T = int(input())

def LCM(A, B):
    cp_A = A
    cp_B = B

    if A < B:
        A, B = B, A
    while (A % B != 0):
        k = A % B
        A = B
        B = k
        if (B == 0):
            B = 1
            break
    print((cp_A // B) * (cp_B // B) * B)
for i in range(T):
    A, B = list(map(int, input().split()))
    LCM(A, B)