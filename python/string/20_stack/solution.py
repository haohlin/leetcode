class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ['[', '(', '{']:
                stack.append(i)
            else:
                if not stack:
                    return False
                prev = stack[-1]
                if self.match(prev, i):
                    stack.pop()
                else: 
                    return False
        if not stack:
            return True
        else:
            return False

    def match(self, a, b):
        if a == '[' and b == ']':
            return True
        elif a == '{' and b == '}':
            return True
        elif a == '(' and b == ')':
            return True
        else:
            return False