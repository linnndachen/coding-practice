class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        if total % 2 != 0:
            return False
        nums.sort()
        target = total//2

        dp = [False] * (target + 1)
        # base case, target = 0 and we have no num left
        dp[0] = True

        for val in nums:
            for weight in range(target, val-1, -1):
                dp[weight] = dp[weight] or dp[weight-val]

        return dp[target]
    """
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)

        if total % 2 != 0:
            return False
        nums.sort()

        self.memo = {}

        return self.top_down(nums, n-1, total//2)

    def top_down(self, nums, idx, cur_left):
        if (idx, cur_left) in self.memo:
            return self.memo[(idx, cur_left)]

        if cur_left == 0:
            return True

        if idx == 0 or cur_left < 0:
            return False

        res = self.top_down(nums, idx-1, cur_left-nums[idx-1]) or \
              self.top_down(nums, idx-1, cur_left)

        self.memo[(idx, cur_left)] = res

        return res
    """
    """
    # backtracking
    def canPartition(self, nums: List[int]) -> bool:
        length, total = len(nums), sum(nums)

        if total % 2 != 0:
            return False

        nums.sort()

        self.memo = {}

        return self.dfs(nums, total // 2, length, 0)

    def dfs(self, nums, goal, length, idx):
        if (idx, goal) in self.memo:
            return self.memo[(idx, goal)]

        if goal == 0:
            return True

        if goal < 0:
            return False

        for i in range(idx, len(nums)):
            if self.dfs(nums, goal-nums[i], length, i+1):
                self.memo[(idx, goal)] = True
                return True
        self.memo[(idx, goal)] = False

        return self.memo[(idx, goal)]
    """