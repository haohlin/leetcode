# 将阿拉伯数字转换为汉语读法
# 4021 ->  四千零二十一

class Solution:
    def maxProfit(self, n):
        positive = True if n > 0 else False
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10

        for i in reversed(range(1,len(digits))):
            cur_digit_c = self.getDigit(i)
            digits.insert(i, cur_digit_c)

        digits = list(reversed(digits))
        pre_zero = False
        result = []
        for i in range(0, len(digits), 2):
            if i == len(digits) - 1:
                if digits[i] == 0:
                    pass
                elif pre_zero:
                    result.append('零')
                    result.append(self.digitToChar(digits[i]))
                elif not pre_zero:
                    result.append(self.digitToChar(digits[i]))
                continue
            
            digit = digits[i]
            # print(digit)
            digit_c = digits[i+1]
            # print(digit_c)
            # print(pre_zero)
            if digit == 0:
                pre_zero = True
                continue
            elif digit != 0 and pre_zero:
                result.append('零')
                pre_zero = False
            result.append(self.digitToChar(digits[i]))
            result.append(digit_c)
                
        return ''.join(result)

    def getDigit(self, n):
        case = n % 4
        if case == 3:
            return '千'
        if case == 2:
            return '百'
        if case == 1:
            return '十'
        if case == 0:
            return '万'

    def digitToChar(self, case):
        if case == 1:
            return '一'
        if case == 2:
            return '二'
        if case == 3:
            return '三'
        if case == 4:
            return '四'
        if case == 5:
            return '五'
        if case == 6:
            return '六'
        if case == 7:
            return '七'
        if case == 8:
            return '八'
        if case == 9:
            return '九'
        if case == 0:
            return '零'



sol = Solution()
result = sol.maxProfit(4021)
print(result)