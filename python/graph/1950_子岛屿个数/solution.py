from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            if m-1 < i or i < 0 or n-1 < j or j < 0 or grid2[i][j] == 0:
                return 
            if grid1[i][j] == 0:
                self.not_include = True
            grid2[i][j] = 0
            for mv in move:
                dfs(i + mv[0], j + mv[1])
            return 
            
        m = len(grid1)
        n = len(grid1[0])
        move = [[0,1],[1,0],[-1,0],[0,-1]]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 0:
                    continue
                self.not_include = False
                dfs(i, j)
                if not self.not_include:
                    count += 1
        return count
