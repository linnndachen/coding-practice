
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # left - prev, right - next
        if not root:
            return root

        prev = dummy = Node(0)
        stack, node = [], root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            node.left, prev.right = prev, node
            prev = node

            node = node.right

        head = dummy.right

        head.left, prev.right = prev, head
        return head