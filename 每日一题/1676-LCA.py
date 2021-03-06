# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        def dfs(root):
            if not root:
                return None
            
            if root in nodes:
                return root
            
            left, right = dfs(root.left), dfs(root.right)
            
            return root if (left and right) else (left or right)
        
        
        return dfs(root)