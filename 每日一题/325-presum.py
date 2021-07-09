from typing import List
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        memo = {}
        res = 0
        cur_sum = 0
        memo[cur_sum] = -1

        for idx, val in enumerate(nums):
            cur_sum += val
            
            if cur_sum - k in memo:
                res = max(res, idx - memo[cur_sum - k])

            if cur_sum not in memo:
                memo[cur_sum] = idx

        return res