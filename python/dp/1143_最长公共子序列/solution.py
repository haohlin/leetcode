class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def findLCS(i, j):
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + findLCS(i + 1, j + 1)
                return dp[i][j]
            if text1[i] != text2[j]:
                dp[i][j] = max(findLCS(i, j + 1),findLCS(i + 1, j))
                return dp[i][j]
        m = len(text1)
        n = len(text2)
        dp = [[-1 for i in range(n)] for j in range(m)]
        result = findLCS(0, 0)
        return result

class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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