from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res, queue = [], deque([root])

        while queue:
            levelsize = len(queue)
            level = []
            
            for _ in range(levelsize):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        
        return res
    """
    # recursive
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        return self.bfs(root, 0, [])
        
        
    def bfs(self, node, level, res):
        # intiate a new level
        if len(res) == level:
            res.append([])
        
        res[level].append(node.val)
        
        if node.left:
            self.bfs(node.left, level + 1, res)
        
        if node.right:
            self.bfs(node.right, level + 1, res)
        
        return res
    """