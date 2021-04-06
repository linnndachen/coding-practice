# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
    
    """
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # recursive
        res = []
        self.dfs(root, res)
        return res
        
        
    def dfs(self, node, res):
        if node:
            res.append(node.val)
            self.dfs(node.left, res)
            self.dfs(node.right, res)
        return res