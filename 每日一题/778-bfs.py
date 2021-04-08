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