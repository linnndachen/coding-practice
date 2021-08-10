class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # 1,5,6,8,9
        # [2,3,4,7,11]
        n = len(arr)
        left, right = 0 , n - 1

        # edge cases - because i have the left + 1 at the end,
        # the answer cannot be the first index
        if k <= arr[0] - 1:
            return k

        while left < right:
            mid = (left+right+1) // 2
            if arr[mid] - mid - 1 < k:
                left = mid
            else:
                right = mid - 1

        return left + 1 + k
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k <= arr[0] - 1:
            return k

        k -= arr[0] - 1

        for i in range(len(arr) - 1):
            miss_count = arr[i+1] - (arr[i]+1)

            if k <= miss_count:
                return arr[i] + k

            k -= miss_count

        return arr[-1] + k
"""