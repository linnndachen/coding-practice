from typing import List
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)

        if s1 > s2:
            return self.minOperations(nums2, nums1)
        if len(nums1) * 6 < len(nums2):
            return - 1

        nums1.sort()
        nums2.sort(reverse=True)

        diff = abs(s1-s2)
        i, j = 0, 0
        res = 0
        while diff > 0:
            if j >= len(nums2) or (i < len(nums1) and 6 - nums1[i] > nums2[j] - 1):
                diff -= 6 - nums1[i]
                i += 1
            else:
                diff -= nums2[j] - 1
                j += 1

            res += 1

        return res