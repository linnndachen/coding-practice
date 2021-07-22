from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (x, y) in enumerate(equations):
            graph[x].append((y, values[i]))
            graph[y].append((x, 1.0/values[i]))

        n = len(queries)
        res = [0] * n
        for i, (x, y) in enumerate(queries):
            if x not in graph or y not in graph:
                res[i] = -1.0

            elif x == y:
                res[i] = 1.0

            else:
                visited = set()
                visited.add(x)
                res[i] = self._dfs(x, y, graph, visited)

        return res

    def _dfs(self, x, y, graph, visited):
        if x == y:
            return 1.0

        for mid, val in graph[x]:

            if mid in visited:
                continue

            visited.add(mid)
            val2 = self._dfs(mid, y, graph, visited)
            if val2 != -1.0:
                return val * val2

        return -1.0