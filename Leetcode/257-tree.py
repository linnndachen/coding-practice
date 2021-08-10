# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # flag: be careful if we store the path as a list or as a string
        # if we store it as a list, we need to use backtrack - pop at the end
        # if we don't want to pop it, we need to append node.val 
        # before the recursion starts
        res = []

        def _dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                # str1 = "->".join(path)
                res.append(path)
            else:
                path += "->"
                if node.left:
                    _dfs(node.left, path)
                
                if node.right:
                    _dfs(node.right, path)

            # path.pop()

        _dfs(root, "")

        return res