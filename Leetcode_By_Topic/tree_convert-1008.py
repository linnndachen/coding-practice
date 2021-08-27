from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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