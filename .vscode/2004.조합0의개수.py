n, m = map(int, input().split())

def check(k, d):
    cnt = 0
    while (k // d != 0):
        k = k // d
        cnt+=k
    return cnt

print(min(check(n,2)-check(n-m,2)-check(m,2), check(n,5)-check(n-m,5)-check(m,5)))