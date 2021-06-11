from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1. be careful of many edge cases - only [0], only [1], [0, 2, 2]
        # 2. the big strucutre - made the mistake of directly doing bfs when meet 2
        m, n = len(grid), len(grid[0])

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    total += 1

        queue = deque()
        rotten = set()      
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((0, i, j))
                    rotten.add((i, j))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  
        res = 0
        while queue:
            steps, x, y = queue.popleft()

            res = steps

            for dx, dy in directions:
                nx, ny = dx+x, dy+y

                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1 and (nx, ny) not in rotten:
                        queue.append((steps+1, nx, ny))
                        rotten.add((nx, ny))

        if total:
            return res if total == len(rotten) else -1

        return 0