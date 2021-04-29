# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> List[List[int]]:
        res = []
        self.dfs(root, summ, [], res)
        return res

    def dfs(self, node, target, path, res):
        if not node:
            return

        path.append(node.val)

        if target == node.val and not node.left and not node.right:
            res.append(list(path))
        else:
            target -= node.val
            if node.left:
                self.dfs(node.left, target, path, res)
            if node.right:
                self.dfs(node.right, target, path, res)

        path.pop()