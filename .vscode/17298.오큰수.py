# import sys
# N = int(input())
# A = list(map(int, sys.stdin.readline().split()))
# out = [-1 for _ in range(1000001)]

# def ft_max(A,i,N):
#     k = A[i]
#     while (i < N-1):
#         if (k < A[i+1]):
#             k = A[i+1]
#         i+=1
#     return k

# for i in range(N-1):
#     if (A[i] < A[i+1]):
#         out[A[i]] = A[i+1]
#     else:
#         a = ft_max(A,i,N)
#         if (A[i] == a):
#             out[A[i]] = -1
#         else:
#             out[A[i]] = a
# A[len(A)-1] = -1
# for num in A:
#     print(out[num], end=' ')

import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
out = [-1 for _ in range(N)]
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        out[stack.pop()] = A[i]
    stack.append(i)
print(*out)