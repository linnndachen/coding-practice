class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or min(nums) == max(nums):
            return 0

        minn, maxn = min(nums), max(nums)
        size = (maxn-minn) // (len(nums)-1) or 1

        buckets = [[None, None] for _ in range((maxn-minn)//size+1)]
        for n in nums:
            b = buckets[(n-minn)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)

        # get ride of empty buckets
        buckets = [items for items in buckets if items[0] is not None]

        return max(buckets[i][0] - buckets[i-1][1] for i in range(1, len(buckets)))