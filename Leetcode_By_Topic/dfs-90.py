from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self._dfs(0, [], nums)

        return self.res

    def _dfs(self, start, cur, nums):
        self.res.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue

            cur.append(nums[i])
            self._dfs(i+1, cur, nums)
            cur.pop()