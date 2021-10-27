import math
class Solution1:
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

class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        if divisor == -1:
            return -dividend if dividend != MIN_INT else MAX_INT
        negitive = False
        if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0):
            negitive = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        count_i = 1
        target_i = dividend
        while target_i >= divisor:
            count_i = 1
            sum_i = divisor
            while sum_i << 1 <= target_i:
                sum_i <<= 1
                count_i <<= 1
            target_i = target_i - sum_i
            count += count_i
        if negitive:
            return -count
        return count



sol = Solution2()
result1 = sol.divide(10,3)
# result2 = sol.div(-5,-2)
# result3 = sol.div(5,-2)

print(2**32)
# print(result2)
# print(result3)