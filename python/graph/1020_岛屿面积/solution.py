from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if m - 1 < i or i < 0 or n - 1 < j or j < 0 or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            self.count += 1
            for mv in move:
                dfs(i + mv[0], j + mv[1])
            return 0

        m = len(grid)
        n = len(grid[0])
        move = [[0,1],[1,0],[-1,0],[0,-1]]
        self.count = 0
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        self.count = 0
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return self.count