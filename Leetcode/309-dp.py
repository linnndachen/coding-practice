class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, rest = float('-inf'), float('-inf'), 0

        for price in prices:
            pre_sold = sold

            # previous held + new profit
            sold = held + price
            # continue to held vs. buy the current stock
            held = max(held, rest - price)
            # continue to rest vs. just sold and must res
            rest = max(rest, pre_sold)

        return max(sold, rest)


#  x x x i

#           previous hold + current price -> sold the stock for money
# sold[i] = hold[i-1] + price[i]

#               continue to hold previous state vs. reset and buy -> enter held state
# held[i] = max(held[i-1], reset[i-1] - price[i])

#               remaind do nothing vs. forced to rest (just sold the day before)
# rest[i] = max(reset[i-1], sold[i-1])

# if i: sold, i-1: buy/keep previous buy status
# if i: buy, i-1: sold/hold
# if i: rest, i-1: sold/keep previous satus

# last i - sell/do nothing