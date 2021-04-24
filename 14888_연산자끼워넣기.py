N = int(input())
A = list(map(int, input().split()))
pm = list(map(int, input().split()))
max_res = -1000000001
min_res = 1000000001
def calculation(idx, res, plus, minus, mul, mod):
    global max_res
    global min_res
    
    if idx == N-1:
        max_res = max(max_res, res)
        min_res = min(min_res, res) 
        return
    if plus:
        calculation(idx+1, res+A[idx+1], plus-1, minus, mul, mod)
    if minus:
        calculation(idx+1, res-A[idx+1], plus, minus-1, mul, mod)
    if mul:
        calculation(idx+1, res*A[idx+1], plus, minus, mul-1, mod)
    if mod:
        if res < 0:
            calculation(idx+1,-(-res//A[idx+1]), plus, minus, mul, mod-1)
        else:
            calculation(idx+1,res//A[idx+1], plus, minus, mul, mod-1)

calculation(0, A[0], pm[0], pm[1], pm[2], pm[3])
print(max_res)
print(min_res)