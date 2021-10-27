# 两数相除

# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

import math



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return math.nan
        divisor_abs = abs(divisor)
        dividend_abs = abs(dividend)
        sum_div = 0
        count = 0
        while True:
            if dividend_abs - sum_div < divisor_abs:
                break
            sum_div += divisor_abs
            count += 1
                
        
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return -count
        else:
            return count


sol = Solution()
result1 = sol.div(-10,0)
# result2 = sol.div(-5,-2)
# result3 = sol.div(5,-2)

print(result1)
# print(result2)
# print(result3)