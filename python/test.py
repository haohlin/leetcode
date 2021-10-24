import math
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left = right = 0
        max_len= 0
        while right < len(s):
            window[s[right]] += 1
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            max_len = max(max_len, right + 1 - left)
            right += 1
        return max_len


sol = Solution()
result = sol.lengthOfLongestSubstring("pwwkew")
print(result)