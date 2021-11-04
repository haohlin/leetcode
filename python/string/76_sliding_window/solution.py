import math
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        res_len = math.inf
        result = ''
        window = defaultdict(int)
        need = defaultdict(int)
        for n in t:
            need[n] += 1
        while right < len(s):
            window[s[right]] += 1
            while self.hasNeed(need, window) and left <= right:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    result = s[left:right+1]
                window[s[left]] -= 1
                left += 1
            right += 1
        return result

    def hasNeed(self, need, window):
        for k, v in need.items():
            if window[k] < v:
                return False
        return True

sol = Solution()
result = sol.minWindow("ADOBECODEBANC", "ABC")
print(result)