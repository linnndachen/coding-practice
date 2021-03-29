from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        res, q = [], deque()

        for idx, val in enumerate(nums):
            # only compare the incoming result
            while q and val > nums[q[-1]]:
                q.pop()

            q.append(idx)
            
            # shrink the window
            if q[0] == idx - k:
                q.popleft()

            # add to the result
            if idx >= k - 1:
                res.append(nums[q[0]])
        return res