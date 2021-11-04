class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        if x == 1:
            return x
        res = 0
        while right >= left:
            mid = left + int((right - left) / 2)
            print(left, mid, right)
            cur_sqr = mid * mid
            if cur_sqr <= x:
                res = mid
                left = mid + 1
            elif cur_sqr > x:
                right = mid - 1
        return res