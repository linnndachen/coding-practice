class Solution:
    """
    sub problem: how many ways I can meet the amount with 0/1/2/3/... coins
    I count the ways, then I plus the cell in amount - coins[i]
    """
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = [0] * (amount + 1)
        memo[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                memo[x] += memo[x - coin]
        
        return memo[amount]