class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        LCS = self.getLongestCommonSubsequence(word1, word2)
        steps = len(word1) + len(word2) - 2 * LCS
        return steps
    def getLongestCommonSubsequence(self, text1: str, text2: str):
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]