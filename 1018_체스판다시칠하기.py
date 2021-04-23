M,N = map(int, input().split())
board = []
for i in range(M):
    here = list(map(str, input()))
    board.append(here)
res = []
for i in range(M-7):
    for j in range(N-7):
        B_change = 0
        W_change = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'B':
                        B_change+=1
                    if board[x][y] != 'W':
                        W_change+=1
                else:
                    if board[x][y] != 'W':
                        B_change+=1
                    if board[x][y] != 'B':
                        W_change+=1
        res.append(B_change)
        res.append(W_change)
print(min(res))    