from typing import List
from collections import deque, defaultdict

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        queue, indegree = deque(), defaultdict(int)
        graph = defaultdict(list)

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for x in range(m):
            for y in range(n):

                for dx, dy in directions:
                    nx = dx+x
                    ny = dy+y
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue

                    if matrix[nx][ny] >= matrix[x][y]:
                        continue
                    indegree[(x,y)] += 1
                    graph[(nx,ny)].append((x, y))

                if indegree[(x, y)] == 0:
                    queue.append((x, y))

        res = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for nb in graph[(i, j)]:
                    indegree[nb] -= 1

                    if indegree[nb] == 0:
                        queue.append(nb)

            res += 1
        return res

    """
    def __init__(self):
        self.res = -1 

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i > 0 and val > matrix[i-1][j] else 0, 
                    dfs(i+1, j) if i < m-1 and val > matrix[i+1][j] else 0,
                    dfs(i, j-1) if j > 0 and val > matrix[i][j-1] else 0,
                    dfs(i, j+1) if j < n-1 and val > matrix[i][j+1] else 0)

            return dp[i][j]

        for x in range(m):
            for y in range(n):
                cur = dfs(x, y)
                self.res = max(self.res, cur)

        return self.res
    """