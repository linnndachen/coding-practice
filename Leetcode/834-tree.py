from typing import List
import collections

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        res = [0] * n
        count = [1] * n

        def postorder(root, prev):
            # to get the size of each subtree
            for i in graph[root]:
                if i != prev:
                    postorder(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def preorder(root, prev):
            # get the dist for the whole tree
            for i in graph[root]:
                if i != prev:
                    # sumDist(b) = sumDist[a] - cnt(b) + cnt[a]
                    res[i] = res[root] - count[i] + (n - count[i])
                    preorder(i, root)

        postorder(0, -1)
        preorder(0, -1)
        return res
