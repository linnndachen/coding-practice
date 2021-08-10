# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time - O(n), only visiting each node once
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        # flag
        self.balanced = True
        self.height(root)
        return self.balanced

    def height(self, root):
        if not root:
            return 0

        left_h = self.height(root.left)
        right_h = self.height(root.right)

        if abs(left_h - right_h) > 1:
            self.balanced = False
            return -1

        return max(left_h, right_h) + 1

    """
    # time - Nlogn, we are actually revisiting nodes
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_dep = self.height(root.left)
        right_dep = self.height(root.right)

        return (abs(left_dep - right_dep) <= 1) and self.isBalanced(root.left) and\
    self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    """