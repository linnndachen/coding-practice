class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [0 for _ in range(n)]
        # base case
        dp[n-1] = 1
        for i in range(n-2, -1, -1):
            newdp = dp[:]
            
            # i == j, dp[i][j] = 1
            newdp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j-1]
                    # dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
                    # dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            dp = newdp

        return dp[n-1]

    """
    def longestPalindromeSubseq(self, s: str) -> int:
        self.memo = {}
        if len(s) == 1:
            return 1
        return self.dfs(s, 0, len(s)-1)

    def dfs(self, s, left, right):
        if (left, right) in self.memo:
            return self.memo[(left, right)]

        if left > right:
            return 0

        if left == right:
            return 1

        if s[left] == s[right]:
            res = 2 + self.dfs(s, left+1, right-1)
        else:
            res = max(self.dfs(s, left+1, right), self.dfs(s, left, right-1))
        self.memo[(left, right)] = res
        return res
    """