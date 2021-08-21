class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once, twice = 0, 0
        for n in nums:
            # not in twice, add to once
            once = ~twice & (once ^ n)
            # add to twice, revert once
            twice = ~once & (twice ^ n)

        return once