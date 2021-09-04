from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def helper(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return 0

            if grid[x][y] == 0 or grid[x][y] == "v":
                return 0

            grid[x][y] = "v"

            return 1 + helper(x+1, y) + helper(x-1, y) + \
                helper(x, y+1) + helper(x, y-1)

        res = 0
        for i in range(m):
            for j in range(n):
                area = helper(i, j)
                res = max(area, res)

        return res
