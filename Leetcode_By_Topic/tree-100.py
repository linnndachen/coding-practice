# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque([(p, q), ])

        def check(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return True

        while queue:
            p1, p2 = queue.popleft()

            if not check(p1, p2):
                return False

            if p1 or p2:
                queue.append((p1.left, p2.left))
                queue.append((p1.right, p2.right))
        return True

    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        queue = deque([(p, q), ])

        while queue:
            node1, node2 = queue.popleft()

            if (not node1 and node2) or (not node2 and node1):
                return False

            if node1 and node2:
                if node1.val != node2.val:
                    return False

                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))

        return True
        """