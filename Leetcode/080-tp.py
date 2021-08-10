class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer, count = 0, 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                pointer += 1
                nums[pointer] = nums[i]
        
        return pointer + 1