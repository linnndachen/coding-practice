from functools import cmp_to_key
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            if y + x > x + y:
                return 1
            elif y + x < x + y:
                return -1
            else:
                return 0
        nums = [str(num) for num in nums]

        res = "".join(sorted(nums, key=cmp_to_key(cmp))).lstrip('0')

        return res if res else "0"