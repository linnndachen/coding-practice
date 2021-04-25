# dp[i][j] = min steps to make s palindrome
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            for i in range(j-1,-1,-1):
                # it needs to be in this order because we must already calculated
                # the value of i+1 and j-1. If reversed, we will cal i then i+1, j then j-1
                dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][n-1] 

    """  
    # 1: another way to write it - interval dp
    n = len(s)
    dp = [[0]*(n) for _ in range(n)]

    # if we start with size 2, be careful of one other edge case.
    # if we have i=0, 0+1 = 1 and 1-1 = 0 (i > j). Here, we default zero
    # so there's not a problem. However, technically, we left out this edge case
    # so it is safest to start with size 3
    for size in range(2, n+1):
        # so that i < j and j < n
        for i in range(n-size+1):
            j = i + size - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    return dp[0][n-1]
    """
    """
    # 2: another way to think about this problem
    # if we say t = s[::-1], it is the same as: shortest common supersequence

    """
    """
    # 3rd way to think about this: find the longest common sequence
    def minInsertions(self, s: str) -> int:
        n = len(s)
        t = s[::-1]
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return n - dp[n][n]  
    """