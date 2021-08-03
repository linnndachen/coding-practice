class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        # the maximum sums so far
        dp[0] = nums[0]
        # stores all the valid indexs before i
        # valid = within k, increasing value
        # the last idx stores the maximum sum so far
        queue = collections.deque([0])

        for end in range(1, len(nums)):
            # pop the old idx (out of range)
            while queue and queue[0] < end - k:
                queue.popleft()
            dp[end] = dp[queue[0]] + nums[end]

            # pop the smaller value
            while queue and dp[end] >= dp[queue[-1]]:
                queue.pop()

            queue.append(end)

        return dp[-1]