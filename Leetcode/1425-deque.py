class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # i < j and j - i <= k, max_sum([list]), list must be non-empty

        queue = collections.deque()
        # current maximum of subsequence
        dp = [0] * len(nums)

        for idx, val in enumerate(nums):
            # out of the range
            while queue and idx - queue[0] > k:
                queue.popleft()

            dp[idx] = val
            if queue:
                dp[idx] = max(dp[idx], dp[queue[0]] + val)

            # new max
            while queue and dp[idx] >= dp[queue[-1]]:
                queue.pop()

            queue.append(idx)
            print(dp, queue)
        return max(dp)