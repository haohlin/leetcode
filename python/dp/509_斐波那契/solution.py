class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        pre_2 = 0
        pre_1 = 1
        res_i = 1
        for i in range(2, n+1):
            res_i = pre_2 + pre_1
            pre_2 = pre_1
            pre_1 = res_i
        return res_i