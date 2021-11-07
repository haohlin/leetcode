from typing import List

class Solution1: # BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        i = j = count = 0
        while i < m:
            j = 0
            while j < n:
                if grid[i][j] != '1' or visited[i][j]:
                    j += 1
                    continue
                queue = [[i,j]]
                visited[i][j] = True
                while queue:
                    loc = queue.pop(0)
                    if loc[1]+1 < n and not visited[loc[0]][loc[1]+1] and grid[loc[0]][loc[1]+1] == '1':
                        queue.append([loc[0], loc[1]+1])
                        visited[loc[0]][loc[1]+1] = True
                    if loc[0]+1 < m and not visited[loc[0]+1][loc[1]] and grid[loc[0]+1][loc[1]] == '1':
                        queue.append([loc[0]+1, loc[1]])
                        visited[loc[0]+1][loc[1]] = True
                    if loc[0]-1 >=0 and not visited[loc[0]-1][loc[1]] and grid[loc[0]-1][loc[1]] == '1':
                        queue.append([loc[0]-1, loc[1]])
                        visited[loc[0]-1][loc[1]] = True
                    if loc[1]-1 >=0 and not visited[loc[0]][loc[1]-1] and grid[loc[0]][loc[1]-1] == '1':
                        queue.append([loc[0], loc[1]-1])
                        visited[loc[0]][loc[1]-1] = True
                j += 1
                count += 1
            i += 1
        return count

class Solution2: # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if m - 1 < i or i < 0 or n - 1 < j or j < 0:
                return 0
            if grid[i][j] != '1':
                return 0
            grid[i][j] = '0'
            for mv in move:
                dfs(i + mv[0], j + mv[1])
            return 1

        m = len(grid)
        n = len(grid[0])
        move = [[0,1],[1,0],[-1,0],[0,-1]]
        i = j = count = 0
        while i < m:
            j = 0
            while j < n:
                count += dfs(i, j)
                j += 1
            i += 1
        return count

sol = Solution2()
sol.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]])