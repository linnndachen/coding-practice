class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = collections.deque()
        minq = collections.deque()

        s = 0
        for n in nums:
            # only keeping the largest and smallest
            while len(maxq) and n > maxq[-1]:
                maxq.pop()

            while len(minq) and n < minq[-1]:
                minq.pop()

            maxq.append(n)
            minq.append(n)
            

            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[s]:
                    maxq.popleft()
                if minq[0] == nums[s]:
                    minq.popleft() 
                s += 1

        return len(nums) - s