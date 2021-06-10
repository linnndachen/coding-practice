class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        seen = set()

        queue = deque([(start[0], start[1])])
        seen.add((start[0], start[1]))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            x, y = queue.popleft()
            if [x, y] == destination:
                return True

            for dx, dy in directions:
                i, j = x, y
                
                while 0 <= i+dx < m and 0 <= j+dy < n and maze[i+dx][j+dy] == 0:
                    i = i+dx
                    j = j+dy

                if (i, j) not in seen:
                    seen.add((i, j))
                    queue.append((i, j))
        return False

    """
    # dfs
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        seen = set()

        seen.add((start[0], start[1]))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(x, y):
            if [x, y] == destination:
                return True

            for dx, dy in directions:
                i, j = x, y

                while 0 <= i+dx < m and 0 <= j+dy < n and maze[i+dx][j+dy] == 0:
                    i = i+dx
                    j = j+dy

                if (i, j) not in seen:
                    seen.add((i, j))
                    
                    if dfs(i, j):
                        return True

            return False

        return dfs(start[0], start[1])
    """
    """
    # for understanding
    def hasPath(self, maze, start, destination):
        return self.helper(maze, destination, start[0], start[1])

    def helper(self, maze, dest, i, j):
        if [i, j] == dest:
            return True
        if maze[i][j] == 2:
            return False

        up, down, left, right = i, i, j, j
        while up > 0 and maze[up-1][j] != 1:
            up -= 1
        while down < len(maze)-1 and maze[down+1][j] != 1:
            down += 1
        while left > 0 and maze[i][left-1] != 1:
            left -= 1
        while right < len(maze[0])-1 and maze[i][right+1] != 1:
            right += 1

        maze[i][j] = 2
        return self.helper(maze, dest, up, j) or self.helper(maze, dest, down, j) or self.helper(maze, dest, i, left) or self.helper(maze, dest, i, right)
    """