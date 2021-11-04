class Solution:
    def calculate(self, s: str) -> int:
        s = list(s.replace(' ', ''))
        def helper(s):
            sign = '+'
            num = 0
            result = []
            while s:
                s_i = s.pop(0)
                if s_i == '(':
                    if sign == '+':
                        result.append(+helper(s))
                    elif sign == '-':
                        result.append(-helper(s))
                if s_i.isdigit():
                    num = num * 10 + int(s_i)
                if not s_i.isdigit() or not s:
                    if sign == '+':
                        result.append(num)
                    elif sign == '-':
                        result.append(-num)
                    num = 0
                    sign = s_i
                if s_i == ')':
                    break
            return sum(result)
        
        return helper(s)