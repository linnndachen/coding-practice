# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        stack = [root]
        i = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node and node.val != voyage[i]:
                return [-1]
            i += 1
            if node.right and node.right.val == voyage[i]:
                if node.left: 
                    res.append(node.val)
                stack.extend([node.left, node.right])
            else:
                stack.extend([node.right, node.left])
        return res
        """
        self.res, self.idx = [], 0
        
        def dfs(node):
            if node:
                print(node.val, self.idx)
                # root node
                if node.val != voyage[self.idx]:
                    self.res = [-1]
                    return

                self.idx += 1

                if node.left and node.left.val != voyage[self.idx]:
                    self.res.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)
                print(self.res)

        dfs(root)
        if self.res and self.res[0] == -1:
            self.res = [-1]
        return self.res
        """