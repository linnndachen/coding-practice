class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        print(dp)
        
        for coin in coins:
            for i in range(coin, amount+1):
                # not include the coin or include the coin
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1