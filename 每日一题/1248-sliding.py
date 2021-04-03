class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        res, start = 0, 0

        for end, num in enumerate(nums):
            # if this was an odd num
            k -= nums[end] % 2

            # used up all odd nums - shrink
            while k < 0:
                k += nums[start] % 2
                start += 1
            res += end - start + 1
        return res