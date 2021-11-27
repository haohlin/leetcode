from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(node):
            if node == len(graph) - 1:
                result.append(path.copy())
            for i in graph[node]:
                path.append(i)
                backtrack(i)
                path.pop()
        result = []
        path = [0]
        backtrack(0)
        return result