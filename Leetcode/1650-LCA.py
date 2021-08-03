"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        
        def traverse_up(root):
            if root is None or root in visited:
                return root
            
            visited.add(root)
            return traverse_up(root.parent)
        
        return traverse_up(p) or traverse_up(q)