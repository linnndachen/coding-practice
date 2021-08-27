from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        stack = [TreeNode(preorder[0])]
        j = 0
        for v in preorder[1:]:
            node = TreeNode(v)
            # 走到leaf, 那一边的分支已经建完的时候
            while stack[-1].val == postorder[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node

            stack.append(node)

        return stack[0]

    """
    # more intuitive solution
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder: 
            return None

        N = len(preorder)

        preD = {val: i for i, val in enumerate(preorder)}
        postD = {val: i for i, val in enumerate(postorder)}


        def buildTree(preLeft, preRight, postLeft, postRight):
            if preLeft == preRight:
                return TreeNode(preorder[preLeft])

            if preLeft > preRight:
                return

            node = TreeNode(preorder[preLeft])

            leftVal,rightVal = preorder[preLeft+1], postorder[postRight-1]

            node.left = buildTree(preLeft+1,preD[rightVal]-1,\
                                      postLeft, postD[leftVal])
            node.right = buildTree(preD[rightVal], preRight, \
                                   postD[leftVal]+1, postRight-1)

            return node

        return buildTree(0,N-1,0,N-1)
    """

    """
    # more efficient solution 
    def __init__(self):
        self.prev_idx = 0
        self.post_idx = 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if self.prev_idx > len(preorder) or self.post_idx > len(postorder):
            return

        root = TreeNode(preorder[self.prev_idx])
        self.prev_idx += 1

        if root.val != postorder[self.post_idx]:
            root.left = self.constructFromPrePost(preorder, postorder)

        if root.val != postorder[self.post_idx]:
            root.right = self.constructFromPrePost(preorder, postorder)

        self.post_idx += 1

        return root
    """