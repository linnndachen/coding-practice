# dp[i][j] = the number of distinct subsequences of s[:i] equals t[:j].
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        if len(s) == len(t):
            return int(s==t)

        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1

        # be VERY careful about which one to loop over first
        # it makes a lot of difference!!!!
        # stuck here for a long time!!!
        for j in range(n+1):
            for i in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]

        """
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    # skip one
                    dp[i][j] = dp[i+1][j] 
        return dp[0][0]
        """