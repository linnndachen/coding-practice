# dp[i][j] = maximum dot product between non-empty subsequences of nums1 and nums2 with the same length
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int
        m, n = len(nums1), len(nums2)

        dp = [[float("-inf")] * (n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                # take i and j, throw all away, only take i, only take j
                dp[i+1][j+1] = max(dp[i][j] + nums1[i]*nums2[j], nums1[i]*nums2[j], dp[i][j+1], dp[i+1][j])

        return dp[-1][-1]