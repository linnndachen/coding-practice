# The value of each non-leaf node = largest leaf value in its left * right subtree
# this question can be soloved by monostack - the most optimized solution
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.memo = {}
        return self.dfs(arr, 0, len(arr)-1)

    def dfs(self, arr, i, j):
        if i >= j:
            return 0

        if (i, j) in self.memo:
            return self.memo[(i, j)]

        res = float('inf')
        for k in range(i+1, j+1):
            # dp(i,j) = dp(i,k) + dp(k+1,j) + value of root.
            res = min(self.dfs(arr,i,k-1) + self.dfs(arr,k,j) + max(arr[i:k]) * max(arr[k:j+1]), res)

        self.memo[(i, j)] = res
        return res