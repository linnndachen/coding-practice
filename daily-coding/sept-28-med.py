"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
"""
def serialize(root):
    # Serialization 
    """ Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    def rserialize(root, string):
        """ a recursive helper function for the serialize() function."""
        # check base case
        if root is None:
            string += 'None,'
        else:
            string += str(root.val) + ','
            string = rserialize(root.left, string)
            string = rserialize(root.right, string)
        return string

    return rserialize(root, '')

def deserialize(root):
    pass