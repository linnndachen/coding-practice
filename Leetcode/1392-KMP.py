class Solution:
    def longestPrefix(self, s: str) -> str:
        # dp[i]: the maximum length k such that s[0:k-1] = s[i-k+1:i]
        # O(n) time complexity if using KMP

        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 0

        # 求后缀数组的5行代码
        for i in range(1, n):
            j = dp[i-1]

            while j >= 1 and s[j] != s[i]:
                j = dp[j-1]
            
            dp[i] = j+ (s[j] == s[i])

        k = dp[n-1]

        return s[:k]