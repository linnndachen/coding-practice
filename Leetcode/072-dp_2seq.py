# dp[i][j] = min operations required to convert word1[:i] to word2[:j].
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # one of the string is empty
        if m * n == 0:
            return n + m

        dp = [[0] * (n+1) for _ in range(m+1)]

        # edges
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 3 options(delete i, insert i, replace)
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[-1][-1]