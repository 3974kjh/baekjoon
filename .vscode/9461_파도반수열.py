T = int(input())
for test in range(T):
    N = int(input())
    wave = [0] * 101
    wave[0] = 1
    wave[1] = 1
    wave[2] = 1
    for i in range(3, N+1):
        wave[i] = wave[i-3] + wave[i-2]
    print(wave[N-1])