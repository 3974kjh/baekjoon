import math
A,B,V = map(int, input().split())
k = V - A
y = A - B
res = math.ceil(k / y)
print(res+1)