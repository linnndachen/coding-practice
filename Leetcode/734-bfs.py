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
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        pq, dist_table = [(0, k)], {}
        
        while pq:
            dist, node = heapq.heappop(pq)
            if node in dist_table:
                continue
            dist_table[node] = dist
            
            for neigh, dist2 in graph[node]:
                if neigh not in dist_table:
                    heapq.heappush(pq, (dist + dist2, neigh))
        
        return max(dist_table.values()) if len(dist_table) == n else -1
  
    # Floyd
    # Time: O(V^3)
    # Space: O(V^2)
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            dist[u-1][v-1] = w
        for i in range(N):
            dist[i][i] = 0

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

        return max(dist[K-1]) if max(dist[K-1]) < float("inf") else -1

        """
    # bfs - dijkstra's algorithm
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