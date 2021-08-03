class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: 
            return []

        m, n = len(heights[0]), len(heights)

        # corrdinates that touch the pacific
        pacific  = [(0, i) for i in range(m)]   + [(i, 0) for i in range(1,n)]
        # coordinates that touch the altantic
        atlantic = [(n-1, i) for i in range(m)] + [(i, m-1) for i in range(n-1)]

        print("pacific", pacific)
        print("atlantic", atlantic)

        return self.bfs(pacific, heights) & self.bfs(atlantic, heights)

    def bfs(self, starts, grid):
        m, n = len(grid[0]), len(grid)
        queue = deque(starts)
        visited = set(starts)
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                # if the inner gird is higher, then it can flow to the outside
                if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visited \
                                                and grid[dx][dy] >= grid[x][y]:
                    queue.append((dx, dy))
                    visited.add((dx, dy))

        return visited
