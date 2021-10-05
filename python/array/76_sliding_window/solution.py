import math
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def windowOK(dict1, dict2):
            if len(dict1) != len(dict2):
                return False
            for k in dict1:
                if dict1[k] < dict2[k]:
                    return False
            return True

        s = list(s)
        t = list(t)
        window = collections.defaultdict(int)
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        start = 0
        end = 0
        min_len = math.inf
        result = []

        while end < len(s):
            # cur_win = s[start:end]
            if s[end] in need:
                window[s[end]] += 1
            while windowOK(window, need):
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    result = s[start:start + min_len]
                if s[start] in need:
                    window[s[start]] -= 1
                    if window[s[start]] == 0:
                        del window[s[start]]
                start += 1
            end += 1

        if min_len == math.inf:
            return ""
        return ''.join(result)

sol = Solution()
result = sol.minWindow("ADOBECODEBANC", "ABC")
print(result)