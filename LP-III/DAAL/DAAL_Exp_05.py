'''
Madhur Jaripatke
Roll No. 52
BE A Computer
RMDSSOE, Warje, Pune
'''
'''
Design n-Queens matrix having first Queen placed. Use backtracking to place remaining 
Queens to generate the final n-queen's matrix.
'''
def is_safe(board, row, col, n):
    # Check if there's a Queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_with_known_first_queen(n, first_queen_row, first_queen_col):
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Place the first Queen at the specified row and column
    board[first_queen_row][first_queen_col] = 1

    def solve_n_queens_util(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                if solve_n_queens_util(row + 1):
                    return True
                board[row][col] = 0

        return False

    if not solve_n_queens_util(first_queen_row + 1):
        print("No solution exists.")
    else:
        for row in board:
            print(row)

n = 8
first_queen_row = 0
first_queen_col = 1
print('For 8x8 Board with 8 queens:\n')
solve_n_queens_with_known_first_queen(n, first_queen_row, first_queen_col)