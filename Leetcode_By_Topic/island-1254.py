from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):

            if x < 0 or y < 0 or x >= m or y >= n:
                return

            if grid[x][y] == 1 or grid[x][y] == "v":
                return

            grid[x][y] = "v"

            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x, y-1)

        for i in range(m):
            for j in range(n):
                if i in {0, m-1} or j in {0, n-1}:
                    dfs(i, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j)

        return res
