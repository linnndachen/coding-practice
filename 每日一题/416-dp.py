class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length, total = len(nums), sum(nums)
        
        if total % 2 != 0:
            return False
        
        memo = [[-1 for x in range(total//2 + 1)] for x in range(length)]
        
        return self.top_down_rec(nums, total // 2, length, memo, 0)
        
    def top_down_rec(self, nums, goal, length, memo, idx):
        if goal == 0:
            return True
        
        if idx >= length or length == 0:
            return False
        
        if memo[idx][goal] == -1:
            if nums[idx] <= goal:
                if self.top_down_rec(nums, goal-nums[idx], length, memo, idx+1):
                    memo[idx][goal] = True
                    return True
                
            memo[idx][goal] = self.top_down_rec(nums, goal, length, memo, idx+1)
        
        return memo[idx][goal]