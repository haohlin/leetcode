class Solution:
    def isLegal(self, s: str):
        queue = []
        for c in s:
            if self.isLeft(c): 
                queue.append(c)
            else:
                if not queue:
                    return False
                left = queue.pop()
                if not self.match(left, c):
                    return False
        if queue:
            return False
        return True
    
    def isLeft(self, c):
        if c in ['[', '(', '{']:
            return True
        else:
            return False

    def match(self, left, right):
        if left == '{' and right == '}':
            return True
        elif left == '(' and right == ')':
            return True
        elif left == '[' and right == ']':
            return True
        else:
            return False

test_1 = '{[]}'
test_2 = '{[}]'
test_3 = ''
test_4 = '}]'
test_5 = '(['

sol = Solution()
result_1 = sol.isLegal(test_1)
result_2 = sol.isLegal(test_2)
result_3 = sol.isLegal(test_3)
result_4 = sol.isLegal(test_4)
result_5 = sol.isLegal(test_5)
