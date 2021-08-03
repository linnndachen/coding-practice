class Solution:
    """
    def winnerSquareGame(self, n: int) -> bool:
        return self.minimax(n)
    @lru_cache(None)
    def minimax(self, remain):
        if remain == 0:
            return False

        sqrt = int(remain ** 0.5)
        for i in range(1, sqrt + 1):
            if not self.minimax(remain - i*i):
                return True
        return False
    """
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        for i in range(1, n+1):
            sqrt = int(i ** 0.5)
            for k in range(1, sqrt+1):
                # if there's one move will can lead to False
                if dp[i - k*k] == False:
                    # I can take the step and make the opponent lose
                    dp[i] = True
                    break

        return dp[n]