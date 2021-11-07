from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if m-1 < i or i < 0 or n-1 < j or j < 0 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            self.local_area += 1
            for mv in move:
                dfs(i + mv[0], j + mv[1])
            return 0

        max_area = 0
        m = len(grid)
        n = len(grid[0])
        move = [[0,1],[1,0],[-1,0],[0,-1]]

        for i in range(m):
            for j in range(n):
                self.local_area = 0
                dfs(i,j)
                max_area = max(max_area, self.local_area)
        return max_area
        