from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i, j, c):
            for col_i in range(9):
                if board[i][col_i] == c:
                    return False
            for row_j in range(9):
                if board[row_j][j] == c:
                    return False
            for row in range((i // 3) * 3, (i // 3) * 3 + 3):
                for col in range((j // 3 ) * 3, (j // 3 ) * 3 + 3):
                    if board[row][col] == c:
                        return False
            return True

        def backtrack(i, j):
            if i >= m:
                return True
            if j >= n:
                return backtrack(i+1, 0)
            if board[i][j] != '.':
                return backtrack(i, j+1)
            
            for c in range(1,10):
                if not isValid(i, j, str(c)):
                    continue
                board[i][j] = str(c)
                if backtrack(i, j+1):
                    return True
                board[i][j] = '.'

            return False
        
        m = len(board)
        n = len(board[0])
        backtrack(0, 0)
