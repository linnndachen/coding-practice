from collections import defaultdict
from math import gcd
import functools

class Solution:
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Find the parent of each node
        parent_graph = defaultdict(int)
        queue = [(0, -1)]
        while queue:
            next_q = []
            for node, parent in queue:
                parent_graph[node] = parent
                for nb in graph[node]:
                    if nb != parent:
                        next_q.append((nb, node))
            queue = next_q

        @functools.lru_cache(None)
        def _dfs(node, node_value):
            if node == -1:
                return -1

            parent = parent_graph[node]

            if gcd(node_value, nums[parent]) == 1:
                return parent

            return _dfs(parent, node_value)

        res = [-1] * len(nums)
        path = defaultdict(list)

        for node in range(len(nums)):
            res[node] = _dfs(node, nums[node])

        return res