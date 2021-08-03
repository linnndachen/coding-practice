# for this question, we need to use heap instead of queue because we can't just
# pop whatever that's on the left of the queue (meaning, either of the children)
# we need to pop/go to with the smallest possible child node. In this sense
# this is similar to dijkstra. However, this is not dijkstra because, we don't need
# to add all values/weights together. We are looking for the smallest-largest weight.
# for example, answer 16 is not the sum of all the nodes but the smallest node that
# allows us to have a path regardless of the "weight"
import heapq
class Solution:
    # bfs + heapq
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, seen, res = len(grid), set([(0, 0)]), 0
        # height, row, cols
        pq = [(grid[0][0], 0, 0)]

        while pq:
            h, r, c = heapq.heappop(pq)
            res = max(res, h)

            if r == n - 1 and c == n - 1:
                return res

            # 4 directions
            for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= i < n and 0 <= j < n and (i, j) not in seen:
                    heapq.heappush(pq, (grid[i][j], i, j))
                    seen.add((i, j))
        return -1 