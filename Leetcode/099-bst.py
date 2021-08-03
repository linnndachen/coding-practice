# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.problem_nodes = []
        self.prev = None

        self.inorder(root)

        if len(self.problem_nodes) == 2:
            self.swap(self.problem_nodes[0][0], self.problem_nodes[1][1])

        elif len(self.problem_nodes) == 1:
            # swap with the root
            self.swap(self.problem_nodes[0][0], self.problem_nodes[0][1])

        return

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        if self.prev and self.prev.val > root.val:
            self.problem_nodes.append((self.prev, root))
        # start with the left node
        self.prev = root
        self.inorder(root.right)
        return
    
    def swap(self, n1, n2):
        n1.val, n2.val = n2.val, n1.val
        return