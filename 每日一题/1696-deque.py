class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        score = [0] * len(nums)
        score[0] = nums[0]
        # enque the index
        queue = collections.deque()
        queue.append(0)

        for end in range(1, len(nums)):
            # pop the old idx (out of range)
            while queue and queue[0] < end - k:
                queue.popleft()
            
            score[end] = score[queue[0]] + nums[end]

            # pop the smaller value
            while queue and score[end] >= score[queue[-1]]:
                queue.pop()

            queue.append(end)

        return score[-1]