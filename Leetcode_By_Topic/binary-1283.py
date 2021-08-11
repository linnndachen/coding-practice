import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # sum([n // ans for n in nums]) <= threshold

        # smallest divisor, largest
        l, r = 1, max(nums)

        while l < r:
            mid = (l + r) // 2
            res = sum([math.ceil(n / mid) for n in nums])
            
            if res <= threshold:
                r = mid
            
            else: # increase divisor
                l = mid + 1

        return r