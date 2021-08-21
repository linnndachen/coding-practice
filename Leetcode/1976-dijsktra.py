from typing import List
import collections, heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # src, dest, cost
        graph = collections.defaultdict(list)

        for src, dest, time in roads:
            graph[src].append((dest, time))
            graph[dest].append((src, time))
        
        dist = [float('inf')] * n
        cnt = [0] * n
        heap = [(0, 0)]

        dist[0] = 0
        cnt[0] = 1

        while heap:
            minCost, dst = heapq.heappop(heap)

            if dist[dst] < minCost:
                continue

            for nb, time in graph[dst]:
                newCost = dist[dst] + time

                if dist[nb] > newCost:
                    dist[nb] = newCost
                    cnt[nb] = cnt[dst]
                    heapq.heappush(heap, (dist[nb], nb))

                elif dist[nb] == dist[dst] + time:
                    cnt[nb] += cnt[dst]

        return cnt[n-1] % (10**9 + 7)