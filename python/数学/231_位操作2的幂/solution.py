class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        if n == 0:
            return False
        while n != 0:
            count += 1
            n = n & (n - 1)
            if count > 1:
                return False
        return True