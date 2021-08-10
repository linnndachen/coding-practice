from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # union find - better solution 不同upscale，直接把 grid 切割为点
        # 同类里面生成线 - 则产生新的区间
        n = len(grid)
        parents = [0]*(n+1)*(n+1)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            if p1 < p2:
                parents[p2] = p1
            else:
                parents[p1] = p2


        # intialize
        for i in range(n+1):
            for j in range(n+1):
                idx = i*(n+1)+j
                parents[idx] = idx

                # connect the boundary
                if i == 0 or i == n or j == 0 or j == n:
                    parents[idx] = 0

        res = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == " ":
                    continue

                # find the index of the connected components
                a, b = 0, 0
                if grid[i][j] == "/":
                    a = i*(n+1)+(j+1)
                    b = (i+1)*(n+1)+(j)
                else:
                    a = i*(n+1)+(j)
                    b = (i+1)*(n+1)+(j+1)

                # union the components tgt
                if find(a) == find(b):
                    res += 1
                else:
                    union(a, b)

        return res


    """
    def regionsBySlashes(self, grid: List[str]) -> int:
        # dfs solution - upscale to 3. If we use 2, then we would need to 
        # check 8 directions instead of 4. The reason is 2 has a problem
        # of dividing the center in example 3.
        # After dividing, this is exactly # 200
        # Complexity: 3*N2 since upscaling

        n, res = len(grid), 0

        # populate the new grid
        new_grid = [[0]*n*3 for _ in range(n*3)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    new_grid[i*3][j*3+2] = new_grid[i*3+1][j*3+1] = new_grid[i*3+2][j*3] = 1
                elif grid[i][j] == "\\":
                    new_grid[i*3][j*3] = new_grid[i*3+1][j*3+1] = new_grid[i*3+2][j*3+2] = 1

        # count the empty cells
        for i in range(n*3):
            for j in range(n*3):
                res += 1 if self.dfs(i, j, new_grid) > 0 else 0

        return res

    def dfs(self, i, j, new_grid):
        if min(i, j) < 0 or max(i, j) >= len(new_grid):
            return 0

        if new_grid[i][j] != 0:
            return 0

        new_grid[i][j] = 1

        return 1 + self.dfs(i-1, j, new_grid) + self.dfs(i+1, j, new_grid) + \
    self.dfs(i, j-1, new_grid) + self.dfs(i, j+1, new_grid)
    """