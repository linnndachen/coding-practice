# minimumAnswer = Math.min(minimumAnswer , Math.abs(totalSum - aSum - aSum));
# goal: to minimize: 
# positive sum - (total sum - positive sum) = 2 * positive sum - total sum
# total sum is all positive sum + all negative sum

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        # weight[i] = stones[i], value[i] = stones[i]
        # so the max
        Max_weight = int(total/2)

        dp = (Max_weight+1)*[0]

        for val in stones:
            for weight in range(Max_weight, -1, -1):
                if weight - val >= 0:
                    dp[weight] = max(val + dp[weight - val], dp[weight])

        return total - 2*dp[-1]


class Solution:
    def lastStoneWeightII(self, stones) -> int:
        sums = set()
        # base case: just 1 stone
        sums.add(stones[0])
        for node in stones[1:]:
            tmpt_sum = set()

            for x in sums:
                tmpt_sum.add(x + node)
                tmpt_sum.add(abs(x - node))
            
            sums = tmpt_sum

        return min(sums)
    
    """
    def lastStoneWeightII(self, stones):
        s = sum(stones)
        dp = [0] * (s + 1)
        # smallest possible sum
        dp[0] = 1
        for i in range(len(stones)):
            for target_sum in range(len(dp)-1, -1, -1):
                if target_sum - stones[i] < 0: 
                    break
                if dp[ target_sum - stones[i] ]:
                    # a possible sum exist
                    dp[target_sum] = 1

        res = s + 1
        for psum in range(1, s+1):
            if dp[psum] and (2 * psum - s >= 0):
                res = min(res, 2*psum-s)
        return res
    """

    """
    # return the smallest possible weights
    class Solution:
        def lastStoneWeightII(self, stones: List[int]) -> int:
            self.memo = {}
            return self.dfs(stones, 0, 0, 0)

        def dfs(self, stones, idx, sum1, sum2):
            if (idx, sum1, sum2) in self.memo:
                return self.memo[(idx, sum1, sum2)]

            # base case: only 1 stone left
            if idx == len(stones):
                return abs(sum1 - sum2)

            left = self.dfs(stones, idx+1, sum1 + stones[idx], sum2)
            right = self.dfs(stones, idx+1, sum1, sum2 + stones[idx])

            res = min(left, right)

            self.memo[(idx, sum1, sum2)] = res

            return res
    """
"""
Main tricks here are to notice that:
        - Given stones = [y1, y2, x1, x2], let's assume we pick y1 - x1 and y2 - x2 in a first pass. 
        - The new stones array is [y1-x1, y2-x2] assuming that x1 and x2 vanished. 
        Then in the second pass, we do (y1 - x1) - (y2 - x2) to get the final answer. 
        
        - Note that we can re-write: (y1 - x1) - (y2 - x2) as (y1 + x2) - (y2 + x1).
        We now notice that what we want is two subarrays of stones that have 
        minimum difference between their sums: min(sp1 - sp2)
        
        - Now note that we can write target = sum(stones) = sp1 + sp2. We can further 
        write the min objective min(sp1 - sp2) = min((sp1 + sp2) - (sp2 + sp2)) = min(target - 2*sp2).
        
        - What value of sp2 will minimize this objective? sp2 = target // 2. 
        So if we can partition the initial stones array into two subarrays of 
        equal sum target // 2, then the final answer is the min = 0. 
        
        - If this partitioning is not possible, partitioning so that sp2 is as 
        close to target // 2 as possible will do.
        
        - Basically we can re-write the min objective min(target - 2 * sp2) = max(sp2) 
        with constraint sp2 <= target // 2
"""