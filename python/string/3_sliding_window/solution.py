from collections import defaultdict

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def nonRepeat(win):
            for val in win.values():
                if val >1:
                    return False
            return True
        # if not s:
        #     return 0
        s = list(s)
        window = defaultdict(int)
        start = end = 0
        max_len = 0
        while end < len(s):
            if nonRepeat(window):
                window[s[end]] += 1
                max_len = max(max_len, len(window))
                end += 1
                continue
            window[s[start]] -= 1
            if window[s[start]] == 0:
                del window[s[start]]
            start += 1
        return max_len

class Solution2:
    # 因为每次只添加最后一个元素，一旦有重复一定是最后一个元素造成的，只需要移动start直到无重复元素为止
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
            
            