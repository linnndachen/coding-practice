from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        t1, t2 = 0, 0

        for n in nums:
            t1, t2 = t2, max(t1 + n, t2)

        return t2