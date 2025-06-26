def check_winer():
    for row in range(BOARD_SIZE):
        if board[row][0] == board[row][1] ==  board[row][2] and board[row][0]:
            return board[row][0]
    for col  in range(BOARD_SIZE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]
    if all(cell for row in board for cell in row):
        return 'нічия'
    return None