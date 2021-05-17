# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # bottom up
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not root.left:
            return root

        old_left_leaf = self.upsideDownBinaryTree(root.left)

        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None

        return old_left_leaf

    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        # top down 
        self.old_left_leaf = None # the new root

        def helper(root, old_parent, old_right_sibling):
            if not root: 
                return
            _left_child = root.left
            _right_child = root.right
            root.left = old_right_sibling
            root.right = old_parent

            if _left_child: 
                helper(_left_child, root, _right_child)
            else:
                self.old_left_leaf = root

        helper(root, None, None)

        return self.old_left_leaf