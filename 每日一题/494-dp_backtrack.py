class Solution:
    def findTargetSumWays(self, A, S):
        count = collections.Counter({0: 1})
        for x in A:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[S]
    
    """
    # memo using dictionary
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        def dfs(nums,i,summary):
            if i == len(nums):
                if summary == S:
                    memo[(i,summary)] = 1
                else:
                    memo[(i,summary)] = 0
            if (i,summary) not in memo:   
                memo[(i,summary)] = dfs(nums,i+1,summary+nums[i]) \
                                    + dfs(nums,i+1,summary-nums[i])
            return memo[(i,summary)]
        dfs(nums,0,0)
        return memo[(0,0)]
    """
    
    
    
    """
    # bottom up
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        if(S not in range(-1 * total, total + 1)): 
            return 0
        dp = [[0 for j in range( total * 2 + 1 )] for i in range(len(nums))]
        
        ## BASE CASE ## FIRST ROW ##
        dp[0][total + nums[0]] += 1
        dp[0][total - nums[0]] += 1
        
        for i in range(1, len(nums)):
            for j in range( total * 2 + 1 ):
                
                if( j - nums[i] >= 0 and dp[i - 1][j - nums[i]] > 0 ): # left side
                    dp[i][j] += dp[i-1][j - nums[i]]
                
                if( j + nums[i] <= total * 2 and dp[i - 1][j + nums[i]] > 0 ): # right side
                    dp[i][j] += dp[i - 1][j + nums[i]]
        
        return dp[-1][total + S]
    """