from typing import List

class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        res = 0
        prev_no, prev_change = 0, 0
        for val in nums:
            cur = max(val*val, prev_no+val*val, prev_change+val)
            no_square = max(val, val+prev_no)
            
            res = max(res, cur)
            prev_no, prev_change = no_square, cur

        return res

    # [2,-1,-4,-3]
    # dp[i][j] = max(dp[i-1][notChanged] + changed, dp[i-1][Changed] + notChanged, self)