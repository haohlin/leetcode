from typing import List

class Solution:
    def numDiffIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if m - 1 < i or i < 0 or n - 1 < j or j < 0 or grid[i][j] != '1':
                return 
            grid[i][j] = '0'
            for mv in move:
                next_i = i + mv[0]
                next_j = j + mv[1]
                if m - 1 >= next_i and next_i >= 0 and n - 1 >= next_j and next_j >= 0 and grid[next_i][next_j] == '1':
                    islands_i.append([mv[0],mv[1]])
                dfs(next_i, next_j)
            return 

        m = len(grid)
        n = len(grid[0])
        move = [[0,1],[1,0],[-1,0],[0,-1]]
        islands = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                islands_i = [[0, 0]]
                dfs(i, j)
                if islands_i not in islands:
                    islands.append(islands_i)
        return len(islands)