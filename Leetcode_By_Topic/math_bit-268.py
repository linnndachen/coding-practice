from typing import List

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            n ^= i^num

        return n

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Gauss' formula
        target = n * (n+1) // 2
        actual = sum(nums)
    
        return target - actual