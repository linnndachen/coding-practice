# boolean dp[i][j]: whether s3[:i+j] is formed by an interleaving of s1[:i] and s2[:j].
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != (l1 + l2):
            return False

        dp = [[False] * (l2+1) for _ in range(l1+1)]
        # because we made it into one-index
        s1, s2, s3 = "#"+s1, "#"+s2, "#"+s3


        dp[0][0] = 1
        # edge cases:
        # if s3 = s1 + s2 or s2+s1
        for i in range(1, l1+1):
            # only comparing s1
            dp[i][0] = dp[i-1][0] == True and s1[i] == s3[i]
        for j in range(1, l2+1):
            # only comparing s2
            dp[0][j] = dp[0][j-1] == True and s2[j] == s3[j]


        for j in range(1, l2+1):
            for i in range(1, l1+1):
                if s1[i] == s3[i+j] and dp[i-1][j] == True:
                    dp[i][j] = True
                elif s2[j] == s3[i+j] and dp[i][j-1] == True:
                    dp[i][j] = True

        return dp[-1][-1]

"""
Logic:

s1: i i i
s2: j j j j j 
s3: z z z z z z z z

The s3[-1] must be either s1[-1] or s2[-1], after we decide the last one,
we wnat to know, if
dp[i-1][j] or dp[i][j-1] can create s[i+j-1]
"""