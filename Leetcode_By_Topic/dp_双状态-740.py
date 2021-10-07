from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        maxi = nums[-1]
        gains = [0 for _ in range(maxi+1)]

        for n in nums:
            gains[n] += n

        prevDelete, prevNotDelete = 0, 0
        for i in range(1, maxi+1):
            Delete = prevNotDelete + gains[i]
            notDelete = max(prevDelete, prevNotDelete)

            prevDelete, prevNotDelete = Delete, notDelete

        return max(prevDelete, prevNotDelete)