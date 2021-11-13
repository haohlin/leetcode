from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(n_left, n_right):
            if n_left < n_right or n_left > n or n_right > n:
                return
            if n_left == n_right and n_left == n:
                result.append(''.join(res))
            
            res.append('(') 
            backtrack(n_left + 1, n_right)
            res.pop()
            
            res.append(')') 
            backtrack(n_left, n_right + 1)
            res.pop()
            return

        result =[]
        res = []
        backtrack(0, 0)
        return result