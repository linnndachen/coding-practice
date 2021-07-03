class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        # min * f(i)
        nums = nums + [float('-inf')]
        stack = []
        res = 0

        for i, val in enumerate(nums):
            while stack and val < nums[stack[-1]]:
                res += i - stack.pop()
            stack.append(i)

        return res