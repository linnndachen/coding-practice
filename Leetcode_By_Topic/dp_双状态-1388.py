from functools import lru_cache
class Solution:
    def maxSizeSlices(self, A):
        @lru_cache(None)
        def dp(i, j, k, cycle=0):
            # i - j search space
            # k - how many times we need to pick
            # cycle: see below
            if k == 1:
                # picking for the last time
                return max(A[i:j + 1])

            if j - i + 1 < k * 2 - 1:
                # boundary check
                return -float('inf')
            # take last element vs. not take last element
            # if take last element, i + 1 because we cannot take the first one
            # else, we skip the element
            return max(dp(i + cycle, j - 2, k - 1) + A[j], dp(i, j - 1, k))

        return dp(0, len(A) - 1, len(A) // 3, 1)
