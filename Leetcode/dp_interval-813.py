# max(score of sum of avg of each group)
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        prefix_sum = [0] * (n+1)
        # dp = [[0] * (K+1) for _ in range(n)]
        memo = {}

        for i in range(n):
            prefix_sum[i+1] = A[i] + prefix_sum[i]

        def avg(i,j):
            ag = (prefix_sum[j] - prefix_sum[i]) / (j - i)
            return ag

        def dfs(idx, k):
            if (idx, k) in memo:
                return memo[(idx, k)]

            if k==1:
                # base case
                return (prefix_sum[-1] - prefix_sum[idx]) / (n - idx)

            res = 0
            for i in range(idx, n-k+1):
                # avg of 0~i + divide what's left into k groups
                res = max(res, avg(idx,i+1) + dfs(i+1, k-1))
            memo[(idx, k)] = res
            return res

        return dfs(0, K)
    """
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)
        prefix_sum = [0] * (N+1)
        for i in range(1, len(A)+1):
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]

        dp = [self._average(prefix_sum, i, N) for i in range(N)]
        print(dp)
        
        # only 1 group, 2 groups and etc
        for k in range(1, min(N, K)):
            for i in range(N):
                # if we have already decided a group, find the rest k
                for j in range(i+1, N):
                    dp[i] = max(dp[i], self._average(prefix_sum, i, j) + dp[j])

        return dp[0]


    def _average(self, prefix_arr, i, j):
        return (prefix_arr[j] - prefix_arr[i]) / float(j - i)
    """

    
# 0..........j j+1.....i (total needs k groups)
# dp[k-1][j]     1 group
# from 0 - j, divide it into k - 1 group