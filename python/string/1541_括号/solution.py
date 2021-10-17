class Solution:
    def minInsertions(self, s: str) -> int:
        left = right = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                left += 1
            if s[i] == ')':
                if left <= 0:
                    right += 1
                else:
                    left -= 1
                if i < len(s) - 1 and s[i+1] == ')':
                    i += 1
                else:
                    right += 1
            i += 1
        return left * 2 + right