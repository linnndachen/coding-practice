from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.idx = 0

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def helper(left, right):
            if self.idx == len(preorder):
                return

            val = preorder[self.idx]
            if val > right or val < left:
                return

            self.idx += 1
            root = TreeNode(val)

            root.left = helper(left, val)
            root.right = helper(val,  right)

            return root
        return helper(float("-inf"), float("inf"))


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:  
        root = TreeNode(preorder[0])
        stack = [root]
        for n in preorder[1:]:
            last = None
            while stack and stack[-1].val < n:
                last = stack.pop()

            node = TreeNode(n)
            if last:
                last.right = node
            elif stack:
                stack[-1].left = node
            stack.append(node)
        return root