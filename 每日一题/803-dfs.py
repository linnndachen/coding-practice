from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Connect unconnected bricks and
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0

            grid[i][j] = 2

            res = 1
            for dx, dy in directions:
                res += dfs(i+dx, j+dy)

            return res

        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            if i == 0:
                return True

            for dx, dy in directions:
                x, y = dx+i, dy+j

                if 0 <= x < m and 0 <= y < n and grid[x][y] == 2:
                    return True

        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1

        # Get grid after all hits
        for i in range(n):
            dfs(0, i)

        # Reversely add the block of each hits and get count of newly add bricks
        ret = [0]*len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and is_connected(i, j):
                ret[k] = dfs(i, j)-1

        return ret
