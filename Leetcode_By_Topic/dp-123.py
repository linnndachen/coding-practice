class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        min_cost = prices[0]
        max_price = prices[-1]
        n = len(prices)
        left_profits = [0] * n
        right_profits = [0] * (n+1)

        for l in range(1, n):
            left_profits[l] = max(left_profits[l-1], prices[l]-min_cost)
            min_cost = min(min_cost, prices[l])

            r = n-1-l
            right_profits[r] = max(right_profits[r+1], max_price - prices[r])
            max_price = max(max_price, prices[r])

        max_profit = 0
        for i in range(0, n):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

        return max_profit

    """
    def maxProfit(self, prices: List[int]) -> int:
        # the reason why we can do it this way is because - what I can do today
        # ony depends on what I did yesterday. What I did in previous days didn't matter.
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            t1_cost = min(t1_cost, price)
            # do nothing - continue to have current profit 
            # or sell the first stock
            t1_profit = max(t1_profit, price - t1_cost)

    
            # if I have sold the first stock
            # do nothing or buy the second stock
            t2_cost = min(t2_cost, price-t1_profit)
            
            # do nothing or sell the stock
            t2_profit = max(t2_profit, price-t2_cost)

        return t2_profit
    """