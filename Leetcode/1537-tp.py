from  typing import List
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2, len1, len2 = 0, 0, len(nums1), len(nums2)
        sum1, sum2, mod = 0, 0, 10 ** 9 + 7
        
        while p1 < len1 or p2 < len2:
            if p1 < len1 and (p2 == len2 or nums1[p1] < nums2[p2]):
                sum1 += nums1[p1]
                p1 += 1
            elif p2 < len2 and (p1 == len1 or nums2[p2] < nums1[p1]):
                sum2 += nums2[p2]
                p2 += 1
            else:
                # when p1 and p2 are the same
                sum1 = sum2 = max(sum1, sum2) + nums1[p1]
                p1 += 1
                p2 += 1
        return max(sum1, sum2) % mod