from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {}
        res = 0
        cur_sum = 0
        memo[cur_sum] = 1
        for val in nums:
            cur_sum += val

            if cur_sum - k in memo:
                res += memo[cur_sum - k]

            if cur_sum in memo:
                memo[cur_sum] += 1
            else:
                memo[cur_sum] = 1

        return res