# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 多个children，先recursion 每个children的路径value， 取出最大的两个加上当前node的value，与output做比较。
# 当前node的返回值是，最大children的value 加上当下node 的value
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.pathsum = float('-inf')
        self.findPath(root)
        return self.pathsum
    def findPath(self, node):
        if not node:
            return 0

        left = max(self.findPath(node.left), 0)
        right = max(self.findPath(node.right), 0)

        self.pathsum = max(self.pathsum, left+right+node.val)

        return max(left, right) + node.val