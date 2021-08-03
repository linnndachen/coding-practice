# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def _dfs(node):
            if not node:
                return 0, float('inf'), float('-inf')

            ln, lmin, lmax = _dfs(node.left)
            rn, rmin, rmax = _dfs(node.right)

            n = float('-inf')
            if node.val > lmax and node.val < rmin:
                n = ln + rn + 1
                self.res = max(self.res, n)

            return n, min(node.val, lmin), max(node.val, rmax)

        _dfs(root)
        return self.res