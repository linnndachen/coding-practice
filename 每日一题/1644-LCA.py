# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.count = 0
        
        def dfs(root, p, q):
            if not root:
                return None
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if (p == root or q == root):
                self.count += 1
                return root
            
            return root if (left and right) else (left or right)
        
        res = dfs(root, p, q)
        
        return res if (self.count == 2) else None