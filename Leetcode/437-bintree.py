# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> int:
        # path: count
        self.memo = {0:1}
        return self.dfs(root, 0, summ)

    def dfs(self, root, prevSum, summ):
        if not root:
            return 0
        count = 0
        cur_sum = prevSum + root.val

        if cur_sum - summ in self.memo:
            # sum of subtree's
            count += self.memo[cur_sum-summ]

        if cur_sum in self.memo:
            self.memo[cur_sum] += 1
        else:
            self.memo[cur_sum] = 1

        # start with different roots
        count += self.dfs(root.left, cur_sum, summ)
        count += self.dfs(root.right, cur_sum, summ)

        self.memo[cur_sum] -= 1
        return count

    """
    # brute force
    def pathSum(self, root: TreeNode, summ: int) -> int:
        if not root:
            return 0
        
        return self.dfs(root, summ) + self.pathSum(root.left, summ) + self.pathSum(root.right, summ)

    def dfs(self, root, summ):
        if not root:
            return 0
        
        summ -= root.val

        return (1 if summ == 0 else 0) + self.dfs(root.left, summ) + self.dfs(root.right, summ)
    """