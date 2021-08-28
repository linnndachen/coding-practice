# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")

        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(" ")
        root = TreeNode(int(data[0]))
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            if data[index] is not '#':
                node.left = TreeNode(int(data[index]))
                queue.append(node.left)

            index += 1
            if data[index] is not '#':
                node.right = TreeNode(int(data[index]))
                queue.append(node.right)

            index += 1
        return root

"""
    def serialize(self, root):
        if not root:
            return "x"

        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        def helper(queue):
            root_val = queue.popleft()
            if root_val == "x":
                return None

            root = TreeNode(int(root_val))
            root.left = helper(queue)
            root.right = helper(queue)
            return root

        lst = deque(data.split(','))

        return helper(lst)
"""
