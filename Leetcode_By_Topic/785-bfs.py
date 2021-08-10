class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = collections.defaultdict(list)

        for v in range(len(graph)):
            if v not in seen:
                # bfs
                queue = collections.deque([v])
                seen[v] = 1
                while queue:
                    node = queue.popleft()

                    for nb in graph[node]:
                        if nb not in seen:
                            seen[nb] = seen[node] * -1
                            queue.append(nb)
                        elif seen[nb] == seen[node]:
                            return False

        return True