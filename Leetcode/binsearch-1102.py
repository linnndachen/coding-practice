import heapq
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(-grid[0][0], 0, 0)] # 最大路径的最小值
        visited = set()
        visited.add((0, 0))

        while pq:
            val, x, y = heapq.heappop(pq)

            if x == m-1 and y == n-1:
                return -val

            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            for dx, dy in directions:
                i = x + dx
                j = y + dy

                if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited:
                    continue

                visited.add((i, j))
                heapq.heappush(pq, (max(-grid[i][j], val), i, j))

        return -1
"""
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left, right = 0, 1000000000
        for x in range(m):
            for y in range(n):
                if grid[x][y] > right:
                    right = grid[x][y]

        while left < right:
            mid = (left+right+1) // 2
            if self._hasPath(mid, grid):
                left = mid
            else:
                right = mid - 1

        return left

    def _hasPath(self, altmin, grid):
        m, n = len(grid), len(grid[0])

        # corner case
        if grid[0][0] < altmin:
            return False

        queue = deque([(0, 0)])
        seen = set(); seen.add((0, 0))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            x, y = queue.popleft()

            # bug， 判断条件放错位置，要注意！
            if x == m-1 and y == n-1:
                return True

            for dx, dy in directions:
                i, j = dx+x, dy+y
                if i < 0 or j < 0 or i >= m or j >= n or (i, j) in seen:
                    continue

                if grid[i][j] >= altmin:
                    queue.append((i, j))
                    seen.add((i, j))

        return False
"""