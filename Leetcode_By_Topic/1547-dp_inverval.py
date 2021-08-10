# [0,1,3,4,5,7]
# 0,1,3    3,4,5,7 #re-add the padding
# the tricky part of this question is boundary/corner cases
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        cuts.sort()
        k = len(cuts)
        dp = [[0] * k for _ in range(k)]

        # at least have 2 in len, so that you can make a cut
        for cut in range(2, k):
            # we don't have the "-1" because we need the padding
            for left in range(k-cut):
                right = left + cut
                
                res = float('inf')
                for m in range(left+1, right):
                    res = min(res, cuts[right]-cuts[left] + dp[left][m] + dp[m][right])
                dp[left][right] = res

        return dp[0][k - 1]