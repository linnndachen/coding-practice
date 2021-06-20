# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else: # start to delete
            # case 1: leaf node
            if not root.left and not root.right:
                root = None

            # case 2: has right child
            # find the node just bigger than this one 
            # thus, smaller than the right and bigger than the left
            # - smallest in the right subtree - sucessor
            elif root.right:
                root.val = self.find_sucessor(root)
                root.right = self.deleteNode(root.right, root.val)

            # case 3: only left child
            # find the node just smaller than this one, so that
            # it is bigger than all the nodes int he left
            # find the largest in the left subtree - presucessor
            else:
                root.val = self.find_prev(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

    def find_sucessor(self, root):
        # the right most branch's lefmost node
        root = root.right
        while root.left:
            root = root.left

        return root.val

    def find_prev(self, root):
        # the left mot branch's right most node
        root = root.left
        while root.right:
            root = root.right

        return root.val


    """
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else: # start to delete
            if not root.left:
                return root.right

            tmp = root.left

            # find the biggest num in the subtree
            while tmp.right:
                tmp = tmp.right

            # replace with the biggest value
            root.val = tmp.val
            # since we have replaced the node we want to delete with the tmp, now we don't
            # want to keep the tmp on this tree, so we just use our function to delete it.
            # pass the val of tmp to the left subtree and repeat the whole approach.
            root.left = self.deleteNode(root.left, tmp.val)

        return root
    """