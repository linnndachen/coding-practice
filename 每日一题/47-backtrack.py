class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        self.backtrack(nums, res, used, [])
        return res

    def backtrack(self, nums, res, used, path):
        if len(path) == len(nums):
            res.append(path[:])
            return 

        for i in range(len(nums)):
            if used[i]:
                continue

            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, res, used, path)

            path.pop()
            used[i] = False