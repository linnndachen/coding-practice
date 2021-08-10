class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = {}
        return self.dfs(text1, text2, 0, 0)

    def dfs(self, s1, s2, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        m, n = len(s1), len(s2)

        if i == m or j == n:
            return 0

        if s1[i] == s2[j]:
            self.memo[(i, j)] = 1 + self.dfs(s1, s2, i+1, j+1)
        else:
            self.memo[(i, j)] = max(self.dfs(s1, s2, i+1, j), self.dfs(s1, s2, i, j+1))

        return self.memo[(i, j)]

    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1),len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for j in reversed(range(n)):
            for i in reversed(range(m)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
    """