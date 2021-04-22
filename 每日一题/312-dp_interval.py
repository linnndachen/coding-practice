class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)

        dp = [[0] * N for _ in range(N)]

        for total_balloons in range(1, N-1):
            for left in range(0, N - total_balloons - 1):
                # creating a range
                right = left + total_balloons + 1
                # iterating within the small range
                for m in range(left+1, right):
                    # same formula to get the best score from (left, right) as before
                    dp[left][right] = max(dp[left][right], nums[left]*nums[m]*nums[right] +\
                                          dp[left][m] + dp[m][right])

        return dp[0][-1]

    """
    def maxCoins(self, nums: List[int]) -> int:
        # if len(set(nums)) == 1:  # edge case when all elements are the same
            # return nums[0] ** 3 * (N - 2) + nums[0] ** 2 + nums[0]

        nums = [1] + nums + [1]
        memo = {}
        return self.dfs(nums, 0, len(nums)-1, memo)

    def dfs(self, nums, left, right, memo):
        if (left, right) in memo:
            return memo[(left, right)]

        if left + 1 >= right:
            return 0

        res = 0
        for k in range(left+1, right):
            res = max(res, nums[k]*nums[left]*nums[right] + \
                      self.dfs(nums, left, k, memo) + self.dfs(nums, k, right, memo))

        memo[(left, right)] = res
        return memo[(left,right)]
    """

#           l   m     r
#      [...,x,x,x,x,x,x,...]

# max coins after the balloons in region (l,m) are burst
# max coins after the balloons in region (m,r) are burst
# nums[l]*nums[m]*nums[r]