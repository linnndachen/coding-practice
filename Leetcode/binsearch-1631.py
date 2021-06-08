import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0

        m, n = len(heights), len(heights[0])
        pq = [(0, 0, 0)]
        res = 0
        visited = set()

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while pq:
            d, x, y = heapq.heappop(pq)

            res = max(res, d)
            visited.add((x, y))

            if (x, y) == (m-1, n-1):
                return res

            for dx, dy in directions:
                i, j = dx+x, dy+y

                if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited:
                    continue

                nd = abs(heights[i][j] - heights[x][y])
                heapq.heappush(pq, (nd, i , j))

        return res

    """
    # binary search
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        left, right = 0, 1000000
        while left < right:
            mid = (left+right) // 2
            if self._hasPath(mid, heights):
                right = mid
            else:
                left = mid + 1
        return left

    def _hasPath(self, altDiff, heights):
        m, n = len(heights), len(heights[0])

        queue, seen = deque([(0, 0)]), set((0, 0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while queue:
            x, y = queue.popleft()

            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in directions:
                i, j = dx+x, dy+y
                if i < 0 or j < 0 or i >= m or j >= n or (i, j) in seen:
                    continue
                diff = abs(heights[i][j] - heights[x][y])
                if diff <= altDiff:
                    queue.append((i, j))
                    seen.add((i, j))

        return False
    """
    # union find
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.parents = {}
        self.rank = {}
        def _find(p):
            if self.parents[p] != p:
                self.parents[p] = _find(self.parents[p])

            return self.parents[p]

        def _union(p, q):
            p1, p2 = _find(p), _find(q)
            if p1 != p2:
                if self.rank[p1] > self.rank[p2]:
                    self.parents[p2] = p1
                elif self.rank[p2] > self.rank[p1]:
                    self.parents[p1] = p2
                else:
                    self.parents[p1] = p2
                    self.rank[p2] += 1

        def _add(p):
            if p not in self.parents:
                self.parents[p] = p
                self.rank[p] = 1

        m, n = len(heights), len(heights[0])

        # edge cases
        if m == 1 and n == 1:
            return 0

        # 1. sort the edges
        edge_list = []
        for i in range(m):
            for j in range(n):
                # right: height difference, x position, y position
                if j != n-1:
                    edge_list.append([abs(heights[i][j] - heights[i][j+1]), i*n+j, i*n+j+1])

                # bottom, x position, y position
                if i != m-1:
                    edge_list.append([abs(heights[i][j] - heights[i+1][j]), i*n+j, (i+1)*n+j])

        edge_list.sort()

        # 2 init
        for i in range(m*n):
            _add(i)

        # 3. union
        for edge in edge_list:
            p, q = _find(edge[1]), _find(edge[2])
            if p != q:
                _union(edge[1], edge[2])
            if _find(0) == _find((m-1)*n + (n-1)):
                return edge[0]
        return 0