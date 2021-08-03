class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len, start = len(nums) + 1, 0
        cur_sum = 0
        
        for end, val in enumerate(nums):
            cur_sum += val
            
            while cur_sum >= s:
                min_len = min(min_len, end - start + 1)
                cur_sum -= nums[start]
                start += 1
                
        return min_len if (min_len != len(nums) + 1) else 0