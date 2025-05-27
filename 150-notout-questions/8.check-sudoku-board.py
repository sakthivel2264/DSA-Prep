
# Example 1
# Input: board =
# [["1","2",".",".","3",".",".",".","."],
# ["4",".",".","5",".",".",".",".","."],
# [".","9","8",".",".",".",".",".","3"],
# ["5",".",".",".","6",".",".",".","4"],
# [".",".",".","8",".","3",".",".","5"],
# ["7",".",".",".","2",".",".",".","6"],
# [".",".",".",".",".",".","2",".","."],
# [".",".",".","4","1","9",".",".","8"],
# [".",".",".",".","8",".",".","7","9"]]

# Output: true
# Example 2
# Input: board =
# [["1","2",".",".","3",".",".",".","."],
# ["4",".",".","5",".",".",".",".","."],
# [".","9","1",".",".",".",".",".","3"],
# ["5",".",".",".","6",".",".",".","4"],
# [".",".",".","8",".","3",".",".","5"],
# ["7",".",".",".","2",".",".",".","6"],
# [".",".",".",".",".",".","2",".","."],
# [".",".",".","4","1","9",".",".","8"],
# [".",".",".",".","8",".",".","7","9"]]

# Output: false

# Check Sudoku board configuration is valid or not – Medium Level
# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

def checkSudoku(board):
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != '.':
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
    return len(res) == len(set(res))


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(checkSudoku(board)) # True