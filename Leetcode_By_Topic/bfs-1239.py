from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        queue = deque([(0, 0, 0)])
        seen = {(0, 0): 0}
        res = 0

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:
            # 注意，这次一定要用for，因为没有用pointer来标记steps
            for _ in range(len(queue)):
                x, y, obs = queue.popleft()

                if x == m-1 and y == n-1:
                    return res

                for dx, dy in directions:
                    nx, ny = dx+x, dy+y

                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue

                    nobs = obs + 1 if grid[nx][ny] == 1 else obs

                    if (nx, ny) in seen and nobs >= seen[(nx, ny)] or (nobs > k):
                        continue

                    queue.append((nx, ny, nobs))
                    seen[(nx, ny)] = nobs
 
            res += 1
        return -1