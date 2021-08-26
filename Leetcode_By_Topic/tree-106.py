from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        memo = {val: i for i, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return

            root_val = postorder.pop()
            root = TreeNode(root_val)

            idx = memo[root_val]

            root.right = helper(idx+1, right)
            root.left = helper(left, idx-1)

            return root

        return helper(0, len(inorder)-1)
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        stack = []

        root = TreeNode(postorder[-1])
        stack.append(root)
        n = len(inorder)
        pos_idx, inor_idx = n-2, n-1

        while pos_idx >= 0:
            node = TreeNode(postorder[pos_idx])
            tmp = None

            while stack and stack[-1].val == inorder[inor_idx]:
                tmp = stack.pop()
                inor_idx -= 1

            if tmp:
                tmp.left = node
            else:
                stack[-1].right = node

            stack.append(node)
            pos_idx -= 1

        return root