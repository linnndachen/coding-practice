class Solution:
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        totalSum = sum(nums)
        if(S not in range(-1 * totalSum, totalSum + 1) ): 
            return 0

        dp = [ [ 0 for j in range( totalSum*2 + 1 ) ] for i in range(len(nums))]

        ## BASE CASE ## FIRST ROW ##
        dp[0][totalSum + nums[0]] += 1
        dp[0][totalSum - nums[0]] += 1
        
        for i in range(1, len(nums)):
            for j in range( totalSum*2 + 1 ):

                # left side
                if( j - nums[i] >= 0 and dp[i-1][j-nums[i]] > 0 ):
                    dp[i][j] += dp[i-1][j-nums[i]]
                
                # right side
                if( j + nums[i] <= totalSum*2 and dp[i-1][j+nums[i]] > 0 ):
                    dp[i][j] += dp[i-1][j+nums[i]]

        return dp[-1][totalSum + S]
    """
    
    """
    class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totals = defaultdict(int)
        totals = {0: 1}
        for num in nums:
            next_totals = defaultdict(int)
            
            for total, count in totals.items():
                next_totals[total+num] += count
                next_totals[total-num] += count
            totals = next_totals
        return totals[target]
    """

    # memo using dictionary
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.memo = {}
        return self.dfs(0, nums, 0, S)

    def dfs(self, cur_sum, nums, idx, target):
        if (idx, cur_sum) in self.memo: 
            return self.memo[(idx, cur_sum)]

        if idx == len(nums):
            return 1 if cur_sum == target else 0

        res = self.dfs(cur_sum - nums[idx], nums, idx+1, target) + \
              self.dfs(cur_sum + nums[idx], nums, idx+1, target)

        self.memo[(idx, cur_sum)] = res

        return res