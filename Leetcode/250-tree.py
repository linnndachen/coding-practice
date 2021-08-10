# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        
        self.check_unival(root)   
        return self.count
    
    def check_unival(self, root):
        if not root:
            return 0

        left = self.check_unival(root.left)
        right = self.check_unival(root.right)

        if (not left or left == root.val) and (not right or right == root.val):
            self.count += 1
            return root.val

        # If current tree is not univalued, the parent tree cannot 
        # be univalued either. So we return a value that the parent 
        # tree's root node can never match.
        return '#'