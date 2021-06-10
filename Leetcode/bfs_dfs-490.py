class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # bfs
        m, n, seen = len(maze), len(maze[0]), set()
        queue = collections.deque([(start[0], start[1])])

        while queue:
            (i, j) = queue.popleft()
            if [i, j] == destination:
                return True
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i, j
                while 0 <= x+dx < m and 0 <= y+dy < n and maze[x+dx][y+dy] == 0:
                    x, y = dx+x, dy+y
                if (x, y) not in seen:
                    seen.add((x, y))
                    queue.append([x, y])

        return False
    """
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # dfs
        m, n, seen = len(maze), len(maze[0]), set()

        def dfs(i, j):
            if [i, j] == destination:
                return True
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i, j
                while 0 <= x+dx < m and 0 <= y+dy < n and maze[x+dx][y+dy] == 0:
                    x, y = dx+x, dy+y
                if (x, y) not in seen:
                    seen.add((x, y))
                    if dfs(x, y):
                        return True

            return False
        return dfs(*start)
    """