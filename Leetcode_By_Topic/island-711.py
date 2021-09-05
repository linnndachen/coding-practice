from typing import List


class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n else 0

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
                grid[i][j] = -1
                islands.append([i, j])
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i-1, j)

        res = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    islands = []
                    dfs(i, j)
                    islands = self.normalize(islands)
                    res.add(islands)

        return len(res)

    def normalize(self, islands):
        res = [[] for _ in range(8)]
        # Rotate and reflect+rotate them against (0,0) in 8 directions.
        for x, y in islands:
            res[0].append([x, y])
            res[1].append([x, -y])
            res[2].append([-x, y])
            res[3].append([-x, -y])
            res[4].append([y, x])
            res[5].append([y, -x])
            res[6].append([-y, x])
            res[7].append([-y, -x])

        for r in res:
            r.sort()
            # normalize it by offseting
            # its smallest coordinate to (0,0)
            x0, y0 = r[0]
            for p in r:
                p[0] -= x0
                p[1] -= y0

        res.sort()

        # Choose the smallest among 8 directions to hash.
        # from "[[x1,y1], [x2,y2], [x3,y3], ...]"=>
        # "(x1, y1, x2, y2, x3, y3, ...)"
        return tuple(c for r in res[0] for c in r)
