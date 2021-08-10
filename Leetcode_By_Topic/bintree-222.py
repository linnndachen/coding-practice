# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftd = self.getDepth(root.left)
        rightd = self.getDepth(root.right)

        if leftd == rightd:
            # all left nodes + count right tree
            return pow(2, leftd) + self.countNodes(root.right)
        else:
            return pow(2, rightd) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0

        return 1 + self.getDepth(root.left)

    """
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        h, node = 0, root

        while node:
            node = node.left
            h += 1

        low, hi = pow(2, h-1), pow(2, h) - 1

        while low < hi:
            # if we only has 2 value, we take the right one
            # to avoid endless loop
            mid = (low+hi) // 2 + 1

            if self.hasK(root, mid):
                low = mid
            else:
                hi = mid - 1

        return low

    # Google interview question - use this func to find out the node nums
    def hasK(self, root, val):
        path = []

        while val > 0:
            path.append(val)
            val //= 2
        for i in range(len(path)-1, -1, -1):
            if not root:
                return False

            if i == 0:
                return True

            if path[i-1] == path[i] * 2:
                root = root.left
            else:
                root = root.right