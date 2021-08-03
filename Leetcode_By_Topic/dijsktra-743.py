# times[i] = [source node, target node, time to travel]
# k: starting point // n: total nums of nodes
# need: total times for n nodes to recieve k

import heapq
class Solution:
    """
    # dijkstra's algorithm - similar, not exact
    # Time - O(E log E) since heap might store E number of 
    # edges and each operation takes log E.
    # Space - O(E) graph and q stores at most E number of entries
    """

    # bfs - dijkstra's algorithm
    def networkDelayTime(self, times, n, k):
        # O(ElogE)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue

            dist[node] = d
            for nb, d2 in graph[node]:
                if nb not in dist:
                    heapq.heappush(pq, (d+d2, nb))

        return max(dist.values()) if len(dist) == n else -1

    def networkDelayTime(self, times, n, k):
        elapsed = [0] + [float("inf")] * n

        graph, queue = defaultdict(list), deque([(0, k)])
        for u, v, w in times:
            graph[u].append((v, w))

        while queue:
            time, node = queue.popleft()
            if time < elapsed[node]:
                elapsed[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))

        mx = max(elapsed)

        return mx if mx < float("inf") else -1
    """
    # dfs
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, N + 1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1
    """