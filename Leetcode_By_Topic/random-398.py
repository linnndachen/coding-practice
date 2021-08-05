import random
from collections import defaultdict
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.indexTable = defaultdict(list)
        for idx, n in enumerate(nums):
            self.indexTable[n].append(idx)

    def pick(self, target: int) -> int:
        positions = self.indexTable[target]
        n = len(positions)
        if n == 1:
            return positions[0]
        else:
            pick = random.randint(0, n-1)
            return positions[pick]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)