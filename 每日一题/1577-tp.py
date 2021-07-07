from typing import List
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # TP solution - suitable for if arr1 and arr2 are sorted
        # similar to 2 sum
        res = 0
        res += self._helper(nums1, nums2)
        res += self._helper(nums2, nums1)
        return res

    def _helper(self, arr1, arr2):
        arr1.sort()
        arr2.sort()

        res = 0

        for x in arr1:
            i = 0; j = len(arr2)-1

            while i < j:
                if x*x > arr2[i] * arr2[j]:
                    i += 1
                elif x*x < arr2[i] * arr2[j]:
                    j -= 1

                else: # we found a valid triplets
                    # 2 corner cases
                    if arr2[i] != arr2[j]:
                        i0 = i; j0 = j

                        while i+1 < j and arr2[i] == arr2[i+1]:
                            i += 1
                        
                        while j-1 > i and arr2[j] == arr2[j-1]:
                            j -= 1

                        res += (i-i0+1) * (j0-j+1)
                        i += 1
                        j -= 1

                    else:
                        tmp = j-i+1
                        res += (tmp * (tmp-1) // 2)
                        break
        return res

    """
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # hashmap: 固定i and j，看有多少个k
        res = 0
        res += self._helper(nums1, nums2)
        res += self._helper(nums2, nums1)

        return res

    def _helper(self, arr1, arr2):
        res = 0

        for a in arr1:
            memo = collections.defaultdict(int)

            for b in arr2:
                if a*a % b == 0:
                    res += memo[a*a // b]

                memo[b] += 1

        return res
    """