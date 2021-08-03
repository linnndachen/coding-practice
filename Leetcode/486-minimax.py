class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        return self.dfs(nums, memo, 0, len(nums) - 1) >= 0


    def dfs(self, nums, memo, i, j):
        if i == j:
            return nums[i]

        if (i, j) in memo:
            return memo[(i, j)]

        # pick the last one - opponent can only pick from i to j-1
        # pick the first one - opponent can only pick from i+1 to j
        memo[(i, j)] = max(nums[j]-self.dfs(nums, memo, i, j-1), \
                           nums[i]-self.dfs(nums, memo, i+1, j))
        return memo[(i, j)]