# 给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t 。

# Case 1: 
#     In: "eceba"
#     out: 3 ("ece")

# Case 2:
#     In: "ccaabbb"
#     out: 5 ("aabbb")
from collections import defaultdict
class Solution:
    def maxSubString(self, s):
        window = dict()
        left = right = 0
        result = ''
        while right < len(s):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1
            if len(window) <=  2:
                result = s[left:right+1] if right + 1 - left > len(result) else result
            while len(window) > 2 and left <= right:
                if window[s[left]] - 1 <= 0:
                    del window[s[left]]
                else:
                    window[s[left]] -= 1
                left += 1
            right += 1
        return result

sol = Solution()
res = sol.maxSubString('ccaabbb')
print(res)