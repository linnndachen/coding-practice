class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        count = 0
        for start_left in range(N):
            for start_right in [start_left, start_left + 1]:
                left, right = start_left, start_right
                while left >= 0 and right < N and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1

        return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n): # abc #cba
                # 两头相等 and (j-i+1) < 3 meaning aba - 中间不等但两头相等
                # or the bigger/outer palidrome is true
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
        return res