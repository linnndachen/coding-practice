# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root)
        return self.count

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        left = left + 1 if node.left and node.left.val == node.val else 0
        right = right + 1 if node.right and node.right.val == node.val else 0

        # we can count both left and right for the answer (confusing question)
        self.count = max(self.count, left+right)

        # for a path, we only return the longest side
        return max(left, right)