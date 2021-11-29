from typing import List

class NumMatrix1:

    def __init__(self, matrix: List[List[int]]):
        self.presum = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix))]
        for i in range(len(self.presum)):
            for j in range(1, len(self.presum[0])):
                self.presum[i][j] = self.presum[i][j-1] + matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            res += self.presum[r][col2 + 1] - self.presum[r][col1]
        return res

class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        self.presum = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        for i in range(1, len(self.presum)):
            for j in range(1, len(self.presum[0])):
                self.presum[i][j] = self.presum[i][j-1] + self.presum[i-1][j] - self.presum[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2+1][col2+1] - self.presum[row2+1][col1] - self.presum[row1][col2+1] + self.presum[row1][col1]