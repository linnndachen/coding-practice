# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        table = {}

        def find_parent(node, parent):
            if not node:
                return

            table[node] = parent
            find_parent(node.left, node)
            find_parent(node.right, node)

        find_parent(root, None)

        visited = set()
        res = []

        def dfs(node, dis):
            if not node or node in visited:
                return

            visited.add(node)

            if dis == K:
                res.append(node.val)
            elif dis < K:
                dfs(node.left, dis+1)
                dfs(node.right, dis+1)
                dfs(table[node], dis+1)

        dfs(target, 0)
        return res

    """
    # build an undirected graph, then level order traversal
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)
        def connect(parent, child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)

            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)
        connect(None, root)

        queue = [target.val]
        seen = set(queue)

        for i in range(K):
            level = []
            for node in queue:
                for nb in graph[node]:
                    if nb not in seen:
                        level.append(nb)
            queue = level
            seen |= set(queue)
        return queue
    """