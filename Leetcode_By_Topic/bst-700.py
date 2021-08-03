# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root and root.val != val:
            if val > root.val:
                root = root.right
            else:
                root = root.left
        
        return root

    """
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root

        else:
            if val > root.val:
                return self.searchBST(root.right, val)
            if val < root.val:
                return self.searchBST(root.left, val)

        return None
    """