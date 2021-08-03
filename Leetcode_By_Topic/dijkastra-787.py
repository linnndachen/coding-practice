# if without the "k stops" restriction, this is exactly dijkstra
# we use pq to make sure we always get the shortest path/lowest cost coming out first
# however, here, we not only need to consider the costs but also how many stops
# so for everything in the pq, it needs to be under the stops
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for s, d, w in flights:
            graph[s].append((w, d))

        pq = [(0, K+1, src)]

        while pq:
            cost, stops, city = heapq.heappop(pq)

            if city is dst:
                return cost

            if stops > 0:
                for cost_to_nb, nb in graph[city]:
                    heapq.heappush(pq, (cost+cost_to_nb, stops-1, nb))

        return -1