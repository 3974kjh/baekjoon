N = int(input())
fibonacci = [0]*1000001
fibonacci[1] = 1
fibonacci[2] = 2
for i in range(3, N+1):
    fibonacci[i] = (fibonacci[i-2] + fibonacci[i-1]) % 15746
print(fibonacci[N])