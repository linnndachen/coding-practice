"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# O(n) of nodes doing width amount of work (width of each level)
# we can upper bound it to O(n) amount of work for n nodes
# O(n^2) will be loose upper bound, b2b compared this to merge sort
# which is O(nlogn)

class Solution:
    def findNext(self, childNode, prev, leftmost):
        if childNode:
            # prev already set up - not the first node on this level
            if prev:
                prev.next = childNode
            else:
                leftmost = childNode
            
            # prev, first node on the next level
            prev = childNode
        
        return prev, leftmost
    
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        leftmost = root
        
        while leftmost:
            prev, curr = None, leftmost
            
            # reset to resign a new leftmost node
            leftmost = None
            
            # iterate the current level
            while curr:
                prev, leftmost = self.findNext(curr.left, prev, leftmost)
                prev, leftmost = self.findNext(curr.right, prev, leftmost)
                
                # move to next level
                curr = curr.next
        
        return root


    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = collections.deque([root])
        
        while queue:
            levelsize = len(queue)
            
            for i in range(levelsize):
                node = queue.popleft()
                
                if i < levelsize - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
    """