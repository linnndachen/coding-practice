class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(0, res, [], nums)
        return res

    def backtrack(self, start, res, curr, nums):
        res.append(curr[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            curr.append(nums[i])
            self.backtrack(i + 1, res, curr, nums)
            curr.pop()

        """
        # subset 1
        class Solution:  
        def subsets(self, nums: List[int]) -> List[List[int]]:
            output = []
            n = len(nums)
            for k in range(n + 1):
                self.backtrack(0, [], k, output, nums)
            return output

        def backtrack(self, start, curr, k, output, nums):
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                self.backtrack(i + 1, curr, k, output, nums)
                curr.pop()
        """