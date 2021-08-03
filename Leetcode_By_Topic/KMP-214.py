class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # essence - find the longest prefix that is a palidrome
        # given p - pattern string, reverse is s
        p, s = s, s[::-1]
        n = len(s)

        if n <= 1:
            return s

        suffix = self.preProcess(p)
        dp = [0 for _ in range(n)]
        dp[0] = p[0] == s[0]

        for i in range(1, n):
            j = dp[i-1]

            while j > 0 and s[i] != p[j]:
                j = suffix[j-1]

            dp[i] = j + (s[i] == p[j])

        k = dp[n-1]
        suf = p[k:]

        return suf[::-1] + p

    def preProcess(self, s):
        n = len(s)
        dp = [0 for _ in range(n)]

        for i in range(1, n):
            # prefix
            j = dp[i-1]

            while j >= 1 and s[i] != s[j]:
                j = dp[j-1]

            dp[i] = j + (s[i] == s[j])

        return dp