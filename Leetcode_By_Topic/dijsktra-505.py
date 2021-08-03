import heapq
from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        pq = [(0, start[0], start[1])]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        seen = {}
        seen[(start[0], start[1])] = 0
        
        while pq:
            d, x, y = heapq.heappop(pq)

            if [x, y] == destination:
                return d

            for dx, dy in directions:
                nx, ny = x, y
                dd = 0
                while 0 <= nx+dx < m and 0 <= ny+dy < n and maze[nx+dx][ny+dy] == 0:
                    nx, ny = nx+dx, ny+dy
                    dd += 1
                # flag: i didn't compare the old val vs. new val
                if (nx, ny) not in seen or d + dd < seen[(nx, ny)]:
                    nd = d + dd
                    seen[(nx, ny)] = nd
                    heapq.heappush(pq, (nd, nx, ny))

        return -1
