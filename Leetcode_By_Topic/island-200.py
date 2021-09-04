from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def helper(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == "0":
                return 

            if grid[x][y] == "v":
                return

            grid[x][y] = "v"
            helper(x+1, y)
            helper(x, y+1)
            helper(x-1, y)
            helper(x, y-1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    helper(i, j)

        return res