# Definition for a binary tree node.
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder or not preorder:
            return None

        val = preorder.pop(0)
        node = TreeNode(val)
        idx = inorder.index(val)

        node.left = self.buildTree(preorder, inorder[:idx])
        node.right = self.buildTree(preorder, inorder[idx+1:])

        return root
    """

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # flag: if not all unique vales, we cannot use hash
        memo = {val: i for i, val in enumerate(inorder)}
        preorder = deque(preorder)

        def _helper(left, right):
            # important
            if left > right:
                return None

            node = preorder.popleft()
            root = TreeNode(node)
            idx = memo[node]
            # flag: if we don't check the last idx, will be wrong answer
            if idx != left:
                root.left = _helper(left, idx - 1)
            if idx != right:
                root.right = _helper(idx + 1, right)
            return root

        return _helper(0, len(inorder) - 1)