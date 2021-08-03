# The value of each non-leaf node = largest leaf value in its left * right subtree

class Solution:
    # 可以转换为next greater element, 因为我们总是先把小的数字处理掉
    def mctFromLeafValues(self, A):
        res = 0
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res

    """
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
            rootVal = max(arr[i:k]) * max(arr[k:j+1])
            # dp(i,j) = dp(i,k) + dp(k+1,j) + value of root.
            res = min(self.dfs(arr,i,k-1) + self.dfs(arr,k,j) + rootVal, res)

        self.memo[(i, j)] = res
        return res
    """