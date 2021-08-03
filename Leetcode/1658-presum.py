class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if total == x:
            return len(nums)

        need = total - x
        prefix = 0
        seen = {0: -1}
        res = 0

        for i, n in enumerate(nums):
            prefix += n

            if prefix - need in seen:
                res = max(res, i - seen[prefix-need])

            seen[prefix] = i

        return len(nums)- res if res else -1

    """
    def minOperations(self, nums: List[int], x: int) -> int:
        # finding the longest subarray with sum(nums) - x
        # similar to the question, if you could replace x nums, longest consec num
        # however, here, we are asking how many nums we can replace/cut off

        total, cur = sum(nums), 0
        maxi, start = -1, 0

        for end, val in enumerate(nums):
            cur += val

            # shrink the window
            while cur > total - x and start <= end:
                cur -= nums[start]
                start += 1

            if cur == total - x:
                maxi = max(maxi, end - start + 1)

        return len(nums) - maxi if maxi != -1 else -1
    """

    """
    # my wrong approach!! - for the record
    min_count, start = float('inf'), 0

    for end, n in enumerate(nums):
        x -= n

        if x == 0:
            min_count = min(min_count, end - start + 1)

        while x < 0:
            x += nums[start]
            start += 1

    return min_count if min_count != float('inf') else -1
    """