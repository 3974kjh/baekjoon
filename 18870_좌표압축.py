import sys
N = int(input())
here = dict()
num = list(map(int, sys.stdin.readline().split()))
num_cp = list(sorted(set(num)))
idx = 0
for i in range(len(num_cp)):
    here[num_cp[i]] = i
for i in num:
    print(here[i], end=' ')
print('')