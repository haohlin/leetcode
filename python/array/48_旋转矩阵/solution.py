from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):
            for j in range(len(matrix[0])):
                matrix[i][j], matrix[-i-1][j] = matrix[-i-1][j], matrix[i][j]
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        