# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'x'
        
        # return (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
        return root.val, self.serialize(root.left), self.serialize(root.right)
        
        # string
        # return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == 'x': 
            return None
        node = TreeNode(data[0])
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])
        return node
    
    """
        def deserialize(self, data):
        # string
		# data stream will be consumed  as we build left side of Tree
		# by the time when the right side is building up, we need to 
        # hold what is left over.
		# Therefore, self.data is a global value, right side will use 
        # what is left over after tree is partially built
        self.data = data
        if self.data[0] == 'x': return None
        node = TreeNode(self.data[:self.data.find(',')]) 
        node.left = self.deserialize(self.data[self.data.find(',')+1:])
        node.right = self.deserialize(self.data[self.data.find(',')+1:])
        return node
    
    """
        