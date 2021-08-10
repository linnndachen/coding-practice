class Solution:
    def minCut(self, s: str) -> int:
        # if s[i,j] is a palindrome, then the minCut(s[:j]) is at most minCut(s[:i-1])+1
        if s == s[::-1]:
            return 0

        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:] == s[i:][::-1]:
                return 1

        # cut numbers in worst case (no palindrome)
        cuts = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            # r stands for radius
            r1, r2 = 0, 0
            # odd palidrome - start from middle
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cuts[i+r1+1] = min(cuts[i+r1+1], cuts[i-r1]+1)
                r1 += 1

            # even palidrome
            while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
                cuts[i+r2+2] = min(cuts[i+r2+2], cuts[i-r2]+1)
                r2 += 1

        return cuts[-1]

    """
    def minCut(self, s: str) -> int:
        # dp[i]: the minimum cuts needed for a palindrome partitioning of[s:i]
        n = len(s)

        isPal = [[False]*n for _ in range(n)]

        # 区间dp， 外层循环考虑区间大小
        for length in range(1, n+1):
            # 内层考虑starting index
            for i in range(n-length + 1):
                j = i + length - 1
                # update isPal[i][j]
                if s[i] == s[j]:
                    # 边界条件, 区间为 1/2 的长度
                    if (i+1) >= (j-1):
                        isPal[i][j] = True
                    else:
                        # 如果外层相等，看里面的是否相等
                        isPal[i][j] = isPal[i+1][j-1]

        dp = [float('inf') for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            for j in range(i+1):
                if isPal[j][i]:
                    if j == 0: # only 1 char
                        dp[i] = 1
                    else:
                        dp[i] = min(dp[i], dp[j-1]+1)

        return dp[n-1] - 1
    """