from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res, queue, direction = [], deque([root]), 1
        
        while queue:
            levelsize = len(queue)
            level = deque()
            
            for _ in range(levelsize):
                node = queue.popleft()
                if direction == 1:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
            direction *= -1
        
        return res
    """
    # recursive
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        return self.bfs(root, 0, 1, [])
    
    def bfs(self, node, level, direction, res):
        if len(res) == level:
            res.append(deque())
        
        if direction == 1:
            res[level].append(node.val)
        else:
            res[level].appendleft(node.val)
        
        if node.left:
            self.bfs(node.left, level + 1, direction * -1, res)
        if node.right:
            self.bfs(node.right, level + 1, direction * -1, res)
        
        return res
    '''