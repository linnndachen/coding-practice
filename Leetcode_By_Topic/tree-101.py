# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = deque([(root.left, root.right), ])

        while queue:
            p1, p2 = queue.popleft()

            if (not p1 and p2) or (not p2 and p1):
                return False

            if p1 and p2:
                if p1.val != p2.val:
                    return False
                queue.append((p1.left, p2.right))
                queue.append((p1.right, p2.left))

        return True


    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.check(root.left, root.right)

    def check(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)
    """