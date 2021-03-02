class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        root_val = root.val
        p_val, q_val = p.val, q.val
        
        if p_val > root_val and q_val > root_val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        elif p_val < root_val and q_val < root_val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else:
            return root