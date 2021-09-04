from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def helper(x, y, sign):
            if x < 0 or y < 0 or x >= m or y >= n:
                return ""

            if grid[x][y] == 0 or grid[x][y] == "v":
                return ""

            grid[x][y] = "v"

            # be cauious of the ending "0" because
            # we need to record where we start to backtrack
            return sign + helper(x+1, y, "r") + helper(x, y+1, "d") + \
                helper(x-1, y, "l") + helper(x, y-1, "u") + "0"

        res = set()
        for i in range(m):
            for j in range(n):
                path = helper(i, j, "s")

                if not path or path in res:
                    continue

                res.add(path)

        return len(res)
