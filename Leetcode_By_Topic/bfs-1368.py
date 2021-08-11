# the way we see this problem is to treat each arrow as cost. Current arrow is 0
# any other direction diff from the arrow will have cost of 1
# so we are finding a path with the lowest cost
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq, visited = [(0, 0, 0)], set()

        while pq:
            cost, i, j = heapq.heappop(pq)

            if (i, j) in visited:
                continue

            visited.add((i, j))

            if (i, j) == (m-1, n-1):
                return cost

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d, (dx, dy) in enumerate(directions, 1):
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    # same direction
                    if d == grid[i][j]:
                        heapq.heappush(pq, (cost, x, y))
                    else:
                        heapq.heappush(pq, (cost + 1, x, y)) 