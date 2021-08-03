from typing import List
class Solution:
    def __init__(self):
        self.res = []
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self._dfs(nums, [], 0)
        return self.res

    def _dfs(self, nums, cur, start):
        if len(cur) >= 2:
            self.res.append(cur[:])

        if cur == len(nums):
            return

        seen = set()

        for i in range(start, len(nums)):
            if cur and nums[i] < cur[-1]:
                continue

            if nums[i] in seen:
                continue

            seen.add(nums[i])
            cur.append(nums[i])
            self._dfs(nums, cur, i+1)
            cur.pop()