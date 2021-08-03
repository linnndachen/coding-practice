class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # [2,6,4,8,10,9,15] left = 6, right = 9
        n = len(nums)
        right_ptr = 0
        big = nums[0]
        for i in range(n):
            if nums[i] < big: 
                right_ptr = i
            else:
                big = nums[i]

        left_ptr = 0
        small = nums[-1]
        for i in range(n-1, -1, -1):
            if nums[i] > small:
                left_ptr = i
            else:
                small = nums[i]

        if right_ptr == left_ptr: 
            return 0
        return right_ptr - left_ptr + 1