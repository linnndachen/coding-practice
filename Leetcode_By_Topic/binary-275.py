class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2 # [0, 1], 0

            if n - mid <= citations[mid]:
                right = mid
            else:
                left = mid + 1
        if n - left <= citations[left]:
            return n - left
        else:
            return 0
