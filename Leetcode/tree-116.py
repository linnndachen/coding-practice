"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    # using pointer
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        leftmost = root
        
        while leftmost.left:
            curr = leftmost
            
            while curr:
                # left to right
                curr.left.next = curr.right
                
                if curr.next:
                    # right to neighour node's left
                    curr.right.next = curr.next.left
                
                # 横着走
                curr = curr.next
            
            # move to the next level
            leftmost = leftmost.left
        
        return root


    """
    # using deque
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        res, queue = [], deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # example of [1,2,3,4,5,6,7]
                # queue[0] would be: (2)3, (4)5, (5)6, (6)7
                # connect everything in this level unless
                # it is the last node
                if i < level_size - 1:
                    node.next = queue[0]
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
    """   