N = int(input())
count = 0
board_row = [0]*N
def check_board(c):
    for i in range(c):
        if board_row[i] == board_row[c]:
            return 0
        if abs(board_row[i] - board_row[c]) == abs(i - c):
            return 0
    return 1
    
def queen(c):
    global count
    if c == N:
        count+=1
        return
    else:
        r = 0
        while r < N:
            board_row[c] = r
            if check_board(c):
                queen(c+1)
            r+=1
queen(0)
print(count)