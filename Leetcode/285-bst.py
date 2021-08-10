# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor
    """
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            node = p.right
            
            while node.left:
                node = node.left
            return node
        else:
            sucessor = None
            while root:
                if p.val < root.val:
                    sucessor = root
                    root = root.left
                else:
                    root = root.right
            return sucessor
    """


    """
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.nodes = []
        self.inorder(root)
        if self.nodes[-1] == p:
            return None
        
        for idx, val in enumerate(self.nodes):
            if val == p:
                return self.nodes[idx+1]

    def inorder(self, root):
        if not root:
            return 

        self.inorder(root.left)
        self.nodes.append(root)
        self.inorder(root.right)
    """