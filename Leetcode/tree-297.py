# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    # bfs
    def serialize(self, root):
        if not root:
            return ''
        queue = collections.deque([root])
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += 'None,'
                continue
            res += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        return res

    def deserialize(self, data):
        if not data:
            return None
        ls = data.split(',')

        root = TreeNode(int(ls[0]))
        queue = collections.deque([root])
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1
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