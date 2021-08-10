class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, cur_end, farthest = 0, 0, 0
        n = len(nums)
        for i in range(n - 1):
            farthest = max(farthest, i+nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest

                if cur_end == (n-1):
                    return jumps
        return jumps

# [2,3,0,1,4] jumps +1 +1
# i = 0, farthest = (0, 2) 2, current_end = 2 *
# i = 1, farthest = (2, 4) 4, current_end = 2 
# i = 2, farthest = (2, 4) 4, current_end = 4 *
# i = 3, farthest = (4, 4) 4, current_end = 4
# i = 4, farthest =           current_end = 4