def nqueens_backtrack(board,row, n):
    for i in range(0,n):
        if (queen_safe(row,i)):
            board[row][i] = True # place queen
            if row(row == n):
                return board
            else:
                nqueens_backtrack(row+1, n)



def queen_safe(row, i):
    pass