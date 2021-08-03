class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # bfs
        m, n = len(maze), len(maze[0])
        seen = {(start[0], start[1]): 0}
        queue =[(0, start[0], start[1])]

        while queue:
            dist, i, j = heapq.heappop(queue)
            if [i, j] == destination:
                return dist
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y, d = i, j, 0
                while 0 <= x+dx < m and 0 <= y+dy < n and maze[x+dx][y+dy] == 0:
                    x, y = dx+x, dy+y
                    d += 1
                if (x, y) not in seen or d + dist < seen[(x, y)]:
                    seen[(x, y)] = dist + d
                    heapq.heappush(queue, (d+dist, x, y))
        return -1