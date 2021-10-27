from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(node):
            if node == len(graph) - 1:
                res = res_i.copy()
                result.append(res)
            for i in graph[node]:
                res_i.append(i)
                backtrack(i)
                res_i.pop()
        result = []
        res_i = [0]
        backtrack(0)
        return result