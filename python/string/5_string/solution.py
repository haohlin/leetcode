class Solution1:
    def longestPalindrome(self, s: str) -> str:
        def growPalindrom(left, right):
            res = []
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res = s[left:right+1]
                left -= 1
                right += 1
            return res
            
        longest = []
        for i in range(len(s)):
            longest_s = growPalindrom(i, i)
            longest_d = []
            if i < len(s) - 1:
                longest_d = growPalindrom(i, i+1)
            
            longest = max([longest, longest_s, longest_d], key=len)
        return longest

    def isPalindrome(self, subs):
        if str(reversed(subs)) == subs:
            return True
        else:
            return False

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        for i in range(len(s)-1):
            res_1 = self.getLongestAtI(s, i, i)
            res_2 = self.getLongestAtI(s, i, i+1)
            max_len_i = res_1 if len(res_1) > len(res_2) else res_2
            result = max_len_i if len(max_len_i) > len(result) else result
        return result
    
    def getLongestAtI(self, s, left, right):
        if s[left] != s[right]:
            return []
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]