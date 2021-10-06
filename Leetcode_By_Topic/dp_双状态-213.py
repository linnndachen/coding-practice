from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        option1 = nums[:-1]
        option2 = nums[1:]
        
        res1, res2 = self.helper(option1), self.helper(option2)
        return max(res1, res2)

    def helper(self, arr):
        t1, t2 = 0, 0

        for n in arr:
            t1, t2 = t2, max(n+t1, t2)

        return t2