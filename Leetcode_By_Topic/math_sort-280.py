class Solution:
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if (i % 2) ^ (nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

    """
    def wiggleSort(self, nums: List[int]) -> None:
        # no sort
        smallTerm = True
        for i in range(len(nums)-1):
            if (smallTerm and nums[i] > nums[i+1]) or \
                (not smallTerm and nums[i] < nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]

            i += 1
            smallTerm = not smallTerm

        return nums

    """


    """
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort(reverse=True)
        for i in range(1, len(nums), 2):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums
    """