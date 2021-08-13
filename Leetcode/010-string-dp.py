class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        s = "#"+s
        p = "#"+p

        m, n = len(s), len(p)
        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1

        for j in range(2, n):
            dp[0][j] = (p[j] == "*" and dp[0][j-2])

        for i in range(1, m):
            for j in range(1, n):
                if s[i] == p[j] or p[j] == ".":
                    dp[i][j] = dp[i-1][j-1]

                elif p[j] == "*":
                    # i-1 needs to match with j because j is a repeat of j-1
                    # and j can represent many j-1
                    opt1 = dp[i-1][j] and (p[j-1] == s[i] or p[j-1] == ".")
                    # when * represents 0, cancel 2 chars
                    opt2 = dp[i][j-2]

                    dp[i][j] = opt1 or opt2

        return dp[m-1][n-1]




class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*":
            return True

        memo = {}

        # i is the length of s and j is the length of p
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    res = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], "."}
                    if j+1 < len(p) and p[j+1] == "*":
                        # we eliminate the current char
                        # or abcdd vs abcd* (last char matched,
                        # we can replicate the last char)
                        res = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        res = first_match and dp(i+1, j+1)

                memo[i, j] = res

            return memo[i, j]

        return dp(0, 0)
