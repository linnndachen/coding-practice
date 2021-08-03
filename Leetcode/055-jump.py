class Solution:
    # note: becareful that you cannot write in reverse
    # it doesn't work to write as - i + nums[i] < next_idx and stop early
    # because you don't know how big previous numbers can be
    def canJump(self, nums: List[int]) -> bool:
        next_idx = len(nums) - 1 # 4
        # second last one
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= next_idx:
                next_idx = i

        return next_idx == 0