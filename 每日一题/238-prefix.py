from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n)
        suffix = [1] * (n)

        for i in range(1, len(prefix)):
            prefix[i] = nums[i-1]*prefix[i-1]

        for j in range(len(suffix)-2, -1, -1):
            suffix[j] = nums[j+1]*suffix[j+1]

        res = [1] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res