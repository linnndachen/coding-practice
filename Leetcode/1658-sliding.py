class Solution:
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
        start, min_count = 0, float('inf')
        current = sum(nums)

        for end, val in enumerate(nums):
            current -= val

            while current < x and start <= end:
                current += nums[start]
                start += 1
            
            if current == x:
                min_count = min(min_count, (len(nums) - 1 - end) + start)

        return min_count if min_count != float('inf') else -1
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