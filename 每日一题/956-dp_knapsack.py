# three options: not pick the rod, put the rod on left, put the rod on right
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # difference: pos side items
        dp = {0:0}

        for x in rods:
            new_dp = {}
            for diff, y in dp.items():
                # init state 
                # ------|----- d -----|      # pos side 
                # - y --|                    # neg  side

                # put x to positive side 
                # ------|----- d -----|---- x --|
                # - y --|
                new_dp[diff+x] = max(new_dp.get(diff+x, 0), y+x)

                # put x to neg side
                # ------|----- d -----|
                # - y --|---- x ---|
                new_dp[diff-x] = max(new_dp.get(diff-x, 0), y)

                # not used
                new_dp[diff] = max(new_dp.get(diff, 0), y)
            dp = new_dp

        return dp[0]

    """
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[idx][summ]: the largest score we can get using rods[j:]
        @lru_cache(None)
        def dp(idx, summ):
            if idx == len(rods):
                return 0 if summ == 0 else float('-inf')
            
            # add to left bucket: summ incraese and left is longer
            # add to right bucket: summ decrease and left unchange
            # not use, add to right, add to left- sum increase and the rods
            return max(dp(idx+1, summ), dp(idx+1, summ-rods[idx]), \
                      dp(idx+1, summ+rods[idx]) + rods[idx])

        # our goal is to find where left(pos bucket) == right(negative bucket)
        # which is zero
        return dp(0, 0)
    """