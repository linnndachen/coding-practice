from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prevSum = {}
        cur = 0

        for idx, val in enumerate(nums):
            cur += val
            self.prevSum[idx] = cur

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prevSum[right]

        return self.prevSum[right] - self.prevSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)