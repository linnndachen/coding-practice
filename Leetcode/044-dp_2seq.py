class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = "#"+s
        p = "#"+p

        m, n = len(s), len(p)
        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1

        for j in range(1, n):
            if p[j] != "*":
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if s[i] == p[j] or p[j] == "?":
                    dp[i][j] = dp[i-1][j-1]

                elif p[j] == "*":
                    # 精髓
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    # for k in range(i+1):
                        # if dp[k][j-1] == 1:
                            # dp[i][j] = 1


        return dp[m-1][n-1]

    # "adceb", 
    # "*a*b"