# useful post for understanding: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/286754/C%2B%2BPython-O(n3)-DP-explanation-%2B-diagrams

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        N = len(values)
        dp = [[0] * N for i in range(N)]

        for vertice in range(2, N):
            for left in range(N-vertice):
                right = left + vertice
                dp[left][right] = float('inf')
                for k in range(left+1, right):
                    dp[left][right] = min(dp[left][right], \
                                          values[k]*values[left]*values[right] + \
                                          dp[left][k] + dp[k][right])

        return dp[0][N-1]

    """
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        return self.dfs(values, memo, 0, len(values)-1)

    def dfs(self, values, memo, left, right):
        if right - left + 1 < 3:
            return 0

        if (left, right) in memo:
            return memo[(left, right)]

        res = float('inf')
        for k in range(left+1, right):
            res = min(res, values[left]*values[right]*values[k] + \
                      self.dfs(values, memo, left, k) + \
                      self.dfs(values, memo, k, right))

        memo[(left, right)] = res

        return memo[(left, right)]
        """