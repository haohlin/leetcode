import math
from typing import List

class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def minPath(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if i >= m or j >= n:
                return math.inf
            if dp[i][j] != -1:
                return dp[i][j]
            down = minPath(i+1, j)
            right = minPath(i, j+1)
            dp[i][j] = min(down, right) + grid[i][j]
            return dp[i][j]
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]
        min_path = minPath(0, 0)
        return min_path

class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                    continue
                pre_left = dp[i][j-1] if j > 0 else math.inf
                pre_up = dp[i-1][j] if i > 0 else math.inf
                dp[i][j] = min(pre_left, pre_up) + grid[i][j]
        return dp[-1][-1]