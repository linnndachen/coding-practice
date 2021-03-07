# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        # find LCA first
        def dfs(node):
            if not node or node.val == p or node.val == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            
            else:
                return left or right
            
        def dist(node, target):
            if not node:
                return float('inf')
            if node.val == target:
                return 0
            return 1 + min(dist(node.left, target), dist(node.right, target))
        
        lca = dfs(root)
        return dist(lca, p) + dist(lca, q)
        
        """
        if p == q:
        return 0
        
        def dfs(root, depth):
            if not root:
                return 0
            
            if p == root.val or q == root.val:
                left = dfs(root.left, 1)
                right = dfs(root.right, 1)
                if left or right:
                    return left or right
                else:
                    return depth
            
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)
            
            if left and right:
                # when they are on the same side
                return left + right - (2 * depth)
            
            return left + right
        
        return dfs(root, 0)
        """