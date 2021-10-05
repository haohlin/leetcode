import math
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        start = 0
        end = len(s1)
        result = []
        window = defaultdict(int)
        need = defaultdict(int)
        for c in s1:
            need[c] += 1
        for d in s2[start:start+end]:
            window[d] += 1

        while end <= len(s2):
            if window == need:
                return True
            if end + 1 > len(s2):
                break
            window[s2[end]] += 1
            window[s2[start]] -= 1
            if window[s2[start]] <= 0:
                del window[s2[start]]
            start += 1
            end += 1
        return False


sol = Solution()
result = sol.checkInclusion("adc", "dcda")
print(result)