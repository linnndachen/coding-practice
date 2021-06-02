class Solution:
    # we need to find "exactly" x numbers in num while h-index is at least x
    # we can also do bucket sort because of the number size - make it O(n)
    def specialArray(self, nums: List[int]) -> int:
        buckets = [0 for _ in range(101)]
        N = len(nums)

        for n in nums:
            buckets[min(n, N)] += 1

        count = 0
        for i in range(N, 0, -1):
            count += buckets[i]

            if count == i:
                return i

        return -1
        
    """
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2 + 1
            count = 0

            for n in nums:
                if n >= mid:
                    count += 1

            if count >= mid:
                left = mid 
            else:
                right = mid - 1

        count = 0
        for n in nums:
            if n >= left:
                count += 1

        if count == left:
            return left

        return -1
    """