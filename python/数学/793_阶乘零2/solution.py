class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        left = self.searchLeft(0, 2 ** 32 - 1, k)
        right = self.searchRight(0, 2 ** 32 - 1, k)
        if left == -1 and right == -1:
            return 0
        return right - left + 1

    def searchLeft(self, start, end, k):
        left = start
        right = end
        while left <= right:
            mid = left + (right - left) // 2
            mid_zeros = self.getZeros(mid)
            if mid_zeros >= k:
                right = mid - 1
            elif mid_zeros < k:
                left = mid + 1
        if left > end or self.getZeros(left) != k:
            return -1
        return left
    
    def searchRight(self, start, end, k):
        left = start
        right = end
        while left <= right:
            mid = left + (right - left) // 2
            mid_zeros = self.getZeros(mid)
            if mid_zeros <= k:
                left = mid + 1
            elif mid_zeros > k:
                right = mid - 1
        if right < 0 or self.getZeros(right) != k:
            return -1
        return right
    
    def getZeros(self, n):
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count