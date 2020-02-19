from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = [set() for i in range(3)]
        rows =  [set() for i in range(9)]
        for row in range(9):
            cols = set()
            for col in range(9):
                if (board[row][col] != '.'):
                    if (board[row][col] in cols or (board[row][col] in square[col//3]) or (board[row][col] in rows[col])):
                        return False
                    else:
                        cols.add(board[row][col])
                        square[col//3].add(board[row][col])
                        rows[col].add(board[row][col])
            if (((row + 1) % 3) == 0):
                print(square)
                square = [set() for i in range(3)]
        return True
