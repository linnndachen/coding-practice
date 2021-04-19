class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        M = 10**9+7

        def dfs(nums):
            if len(nums) <= 2: 
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            
            # C(m+n, m/n)
            return math.comb(len(left)+len(right), len(right)) * dfs(left) * dfs(right) % M

        # -1 to exclude the original order
        return dfs(nums)-1