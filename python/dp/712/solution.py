class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def getMin(i, j):
            if i >= m:
                res = 0
                for k in range(j, n):
                    res += ord(s2[k])
                return res
            if j >= n:
                res = 0
                for k in range(i, m):
                    res += ord(s1[k])
                return res
            if dp[i][j] != -1:
                return dp[i][j]
            if s1[i] == s2[j]:
                dp[i][j] = getMin(i+1, j+1)
                return dp[i][j]
            else:
                dp[i][j] = min(getMin(i, j+1) + ord(s2[j]), getMin(i+1, j) + ord(s1[i]))
                return dp[i][j]

        m = len(s1)
        n = len(s2)
        dp = [[-1 for i in range(n)] for j in range(m)]
        result = getMin(0, 0)
        return result

