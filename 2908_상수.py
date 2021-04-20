A, B = input().split()
A = list(map(str, A))
B = list(map(str, B))
A.reverse()
B.reverse()
res_A = "".join(A)
res_B = "".join(B)
if res_A > res_B:
    print(res_A)
else:
    print(res_B)