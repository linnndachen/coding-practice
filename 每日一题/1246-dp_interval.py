class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [[float('inf')]*N for _ in range(N)]

        for i in range(N):
            # i == j
            dp[i][i] = 1

        # prefill to avoid
        # avoid edge cases like only has only 2 elements
        for i in range(N-1):
            if arr[i] == arr[i+1]:
                dp[i][i+1] = 1
            else:
                dp[i][i+1] = 2

        for size in range(3, N+1):
            for left in range(N-size+1):
                right = left + size - 1
                if arr[left] == arr[right]:
                    dp[left][right] = dp[left+1][right-1]
                for mid in range(left, right):
                    dp[left][right] = min(dp[left][right], dp[left][mid]+dp[mid+1][right])
        return dp[0][N-1]

    """
    def minimumMoves(self, arr: List[int]) -> int:
        self.memo = {}

        return self.dfs(arr, 0, len(arr)-1)

    def dfs(self, arr, left, right):
        if left > right:
            return 0
        # first n to remove is the last one
        # thus, the range because [0: -2]
        res = self.dfs(arr, left, right-1) + 1
        if arr[right] == arr[right-1]:
            res = min(res, self.dfs(arr,left, right-2) + 1)

        # scan the range to find the palidrome of "right"
        for k in range(left, right-1):
            if arr[right] == arr[k]:
                res = min(res, self.dfs(arr,left, k-1) + self.dfs(arr,k+1, right-1))
        return res
    """