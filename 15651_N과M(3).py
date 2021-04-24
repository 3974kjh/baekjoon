N,M = map(int, input().split())
count = 0
board_row = [0]*M

def check_board(c):
    for i in range(c):
        if board_row[i] > board_row[c]:
            return 0
    return 1

def check(c):
    global count
    if c == M:
        for i in board_row:
            print(i, end=' ')
        print('')
        return
    else:
        r = 1
        while r <= N:
            board_row[c] = r
            if check_board(c):
                check(c+1)
            r+=1
check(0)