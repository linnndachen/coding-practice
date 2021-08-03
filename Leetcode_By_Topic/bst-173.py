# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # Space - O (h)
    def __init__(self, root: TreeNode):
        self.stack = []
        self._inorderL(root)

    def _inorderL(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._inorderL(node.right)
        return node.val

    def hasNext(self) -> bool:
        return True if self.stack else False

    """
    # Space O(n)
    def __init__(self, root: TreeNode):
        self.nodes = []
        self._inorder(root)
        self.index = -1

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes)
    """


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()