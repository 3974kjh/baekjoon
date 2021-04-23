# def draw_star(n):
#     global Map
#     if n == 3:
#         Map[0][:3] = Map[2][:3] = [1]*3
#         Map[1][:3] = [1, 0, 1]
#         return

#     a = n//3
#     draw_star(n//3)
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             for k in range(a):
#                 Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]

# N = int(input())
# Map = [[0 for i in range(N)] for i in range(N)]
# draw_star(N)

# for i in Map:
#     for j in i:
#         if j:
#             print('*', end = '')
#         else:
#             print(' ', end = '')
#     print()

N = int(input())
map = [[0] * N for _ in range(N)]
def star(N):
    global map
    if N == 3:
        map[0][:1] = map[2][:1] = [1]*3
        map[1][:1] = [1,0,1]
        return
    n = N // 3
    star(n)
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            for k in range(n):
                map[n*i + k][n*j:n*(j+1)] = map[k][:n]
star(N)
for x in range(N):
    for y in range(N):
        if map[x][y] == 1:
            print('*',end='')
        elif map[x][y] == 0:
            print(' ',end='')
    print('')