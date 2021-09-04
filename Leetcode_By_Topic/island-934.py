from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return

            if grid[x][y] == "v" or grid[x][y] == 0:
                return

            grid[x][y] = "v"
            queue.append((x, y, 0))

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        found = False
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

            if found:
                break

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j, steps = queue.popleft()

            for dx, dy in directions:
                nx, ny = dx+i, dy+j

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                if grid[nx][ny] == "v":
                    continue

                if grid[nx][ny] == 1:
                    return steps

                grid[nx][ny] = "v"
                queue.append((nx, ny, steps+1))

        return -1
