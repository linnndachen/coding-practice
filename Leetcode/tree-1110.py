# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        delete_set = set(to_delete)
        res = []

        def helper(node, is_root):
            if not node:
                return None

            root_deleted = node.val in delete_set

            if is_root and not root_deleted:
                res.append(node)

            node.left = helper(node.left, root_deleted)
            node.right = helper(node.right, root_deleted)

            return None if root_deleted else node

        helper(root, True)
        return res

    """
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # bottom up
        res = []
        delete_set = set(to_delete)

        def _dfs(node):
            if not node:
                return None

            node.left = _dfs(node.left)
            node.right = _dfs(node.right)

            if node.val in delete_set:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)

                # flag: directly return the node
                return None

            return node

        _dfs(root)
        if root.val not in delete_set:
            res.append(root)

        return res
    """