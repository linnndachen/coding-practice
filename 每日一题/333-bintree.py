# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class subtree():
    def __init__(self, largest, n, mini, maxi):
        self.largest = largest   # largest bst
        self.count = n           # number of nodes in this subtree
        self.mini = mini      # min val in the substree
        self.maxi = maxi     # max val in teh subtree

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res.largest

    def dfs(self, node):
        if not node:
            return subtree(0, 0, float('inf'), float('-inf'))

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if node.val > left.maxi and node.val < right.mini:
            n = left.count + right.count + 1
        else:
            n = float('-inf')

        largest = max(left.largest, right.largest, n)

        return subtree(largest, n, min(left.mini, node.val), max(right.maxi, node.val))