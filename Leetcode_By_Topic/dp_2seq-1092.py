class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for j in range(n):
            for i in range(m):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        i, j, res = m-1, n-1, []
        while i >= 0 and j >= 0:
            if str1[i] == str2[j]:
                res.append(str1[i])
                i -= 1
                j -= 1
                # the larger dp value is part of lca
                # so append the missing out char
            elif dp[i+1][j] < dp[i][j+1]:
                res.append(str1[i])
                i -=1
            else:
                res.append(str2[j])
                j -= 1
                # extra char + LCA
        return str1[:i+1] + str2[:j+1] + "".join(reversed(res))