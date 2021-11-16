class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        dp = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(i+1):
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        for i in reversed(range(size - 1)):
            for j in range(i+1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j]) 
        return dp[0][size-1]