"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

 #O(n^2)
 def is_unival(root):
    return unival_helper(root, root.value)

def unival_helper(root, value):
   if root is None:
      return True
   if root.value 