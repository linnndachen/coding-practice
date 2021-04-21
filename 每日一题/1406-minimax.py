class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # Alice - Bob at every index
        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
            dp[i] = float('-inf')

            tmpt_score = 0
            for k in range(min(3, n-i)):
                tmpt_score += stoneValue[i+k]
                dp[i] = max(dp[i], tmpt_score - dp[i+k+1])

        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"

    """
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = [0] * len(stoneValue)
        score = self.minimax(stoneValue, 0, memo)
        if score == 0:
            return "Tie"
        elif score > 0:
            return "Alice"
        else:
            return "Bob"

    def minimax(self, stoneValue, idx, memo):
        n = len(stoneValue)
        if idx >= n:
            return 0

        if memo[idx] != 0:
            return memo[idx]

        res = float('-inf')
        tmpt_score = 0
        for i in range(idx, min(n, idx + 3)):
            tmpt_score += stoneValue[i]
            res = max(res, tmpt_score - self.minimax(stoneValue, i+1, memo))

        memo[idx] = res

        return memo[idx]
    """