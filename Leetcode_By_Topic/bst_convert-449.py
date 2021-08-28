# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # preorder + lower/upper bound (1008 code)
    # preorder + (preorder, inorder)
    # note: 297 can use bfs, but I dont think this one can

    """
    def serialize(self, root):
        # preorder
        res, stk = [], []
        while stk or root:
            if root:
                res.append(str(root.val))
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                root = root.right
        return ' '.join(res)


    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return
        data = data.split(" ")
        node = root = TreeNode(int(data[0]))
        stack = []
        for char in data[1:]:
            n = int(char)
            while stack and stack[-1].val < n:
                node = stack.pop()

            if n < node.val:
                node.left = TreeNode(n)
                stack.append(node)
                node = node.left
            else:
                node.right = TreeNode(n)
                node = node.right
        return root
    """

    def serialize(self, root: TreeNode) -> str:

        def preorder(node):
            if not node:
                return ""

            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        vals = []
        preorder(root)

        return " ".join(vals)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return

        data = data.split(" ")
        self.i = 0

        def helper(left, right):
            if self.i == len(data):
                return

            val = int(data[self.i])
            if val < left or val > right:
                return

            root = TreeNode(val)
            self.i += 1
            root.left = helper(left, root.val)
            root.right = helper(root.val, right)

            return root

        return helper(float("-inf"), float("inf"))
