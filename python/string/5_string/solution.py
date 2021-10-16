class Solution:
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