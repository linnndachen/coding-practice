class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # dp[i][u] = max(dp[i-1][u], dp[i-1][o]) + 1
        # dp[i][a] = max(dp[i-1][_], dp[i-1][a]) + 1
        # 在 i position上，以j字母结尾，最长的beautiful string
        # dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        
        dp = [float('-inf') for _ in range(6)] # _,a,e,i,o,u
        dp_prev = [float('-inf') for _ in range(6)]
        Atoi_map = {"a":1, "e":2, "i":3, "o":4, "u":5}

        dp[0] = 0
        res = 0
        for i in range(len(word)):
            for j in range(6):
                dp_prev[j] = dp[j]

            for j in range(1, 6):
                if Atoi_map[word[i]] == j:
                    dp[j] = max(dp_prev[j], dp_prev[j-1]) + 1
                else:
                    dp[j] = float('-inf')

            res = max(res, dp[5])

        return res

    """
    def longestBeautifulSubstring(self, word: str) -> int:
        # greedy
        seen = set()
        left = 0
        res = 0
        for right, char in enumerate(word):
            if right > 0 and char < word[right-1]:
                seen = set()
                left = right

            seen.add(char)
            if len(seen) == 5:
                res = max(right-left+1, res)

        return res
    """