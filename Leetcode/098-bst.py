# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -float('inf'), float('inf'))]
        while stack:
            node, low, hi = stack.pop()
            if not node:
                continue

            if node.val >= hi or node.val <= low:
                return False

            stack.append((node.right, node.val, hi))
            stack.append((node.left, low, node.val))

        return True

    def validate(self, low, hi, node):
        if not node:
            return True

        if node.val >= hi or node.val <= low:
            return False
        
        return self.validate(low, node.val, node.left) and \
    self.validate(node.val, hi, node.right)


    """
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = -float('inf')
        return self.inorder(root)

    def inorder(self, root):
        if not root:
            return True

        if not self.inorder(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        return self.inorder(root.right)
    """