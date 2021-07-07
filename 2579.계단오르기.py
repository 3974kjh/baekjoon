N = int(input())
A = [0 for i in range(301)]
B = [0 for i in range(301)]
for i in range(N):
    A[i] = int(input())
B[0] = A[0]
B[1] = A[0] + A[1]
B[2] = max(A[1] + A[2], A[0] + A[2])
for i in range(3, N):
    B[i] = max(A[i] + A[i-1] + B[i-3], A[i] + B[i-2])
print(B[N-1])