# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """       
        using inorder to construct the tree while using postorder to find the root.
        Property of inorder is that the root node will always be in the middle
        """

        # save the index of each node in inorder
        map_inorder = {}
        for i, val in enumerate(inorder): 
            map_inorder[val] = i


        def helper(low, high):
            # base case: no nodes to visit
            if low > high: 
                return None

            # find the root
            root = TreeNode(postorder.pop())

            # construct the tree
            mid = map_inorder[root.val]
            
            root.right = helper(mid + 1, high)
            root.left = helper(low, mid - 1)

            return root

        return helper(0, len(inorder)-1)

    # optimized
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """       
        using inorder to construct the tree while using postorder to find the root.
        Property of inorder is that the root node will always be in the middle
        """

        def helper(left, right):
            if left > right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            idx = inorder_map[val]
            
            root.right = helper(idx+1, right)
            root.left = helper(left, idx-1)

            return root

        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        return helper(0, len(inorder)-1)