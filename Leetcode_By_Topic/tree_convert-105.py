# Definition for a binary tree node.
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # flag: if not all unique vales, we cannot use hash
        memo = {val: i for i, val in enumerate(inorder)}
        preorder = deque(preorder)

        def _helper(left, right):
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


    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)

        prev_idx = 1
        inor_idx = 0


        while prev_idx < len(preorder):
            node = TreeNode(preorder[prev_idx])
            prev_idx += 1
            prev = None

            while stack and stack[-1].val == inorder[inor_idx]:
                prev = stack.pop()
                inor_idx += 1

            if prev:
                prev.right = node
            else:
                stack[-1].left = node


            stack.append(node)

        return root