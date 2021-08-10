class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # for each building 1, run BFS and record for each 0
        # the distance from that building 1 + how many buildings it can reach
        # the optimal new building spot is the 0 that has least total distance
        n, m = len(grid), len(grid[0])
        buildings = sum(grid[x][y] for x in range(n) for y in range(m) if grid[x][y] == 1)

        # used dict instead of matrix - faster
        # each (x, y) of zeros: distance to reach each building 1
        distance = collections.defaultdict(list)
        # run BFS on every node where the value is 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if not self.bfs(i, j, distance, grid, buildings):
                        return -1

        ret = float('+inf')
        for (i, j), distances in distance.items():
            if len(distances) == buildings:
                # find the least distance
                ret = min(ret, sum(distances))
        return -1 if ret == float('+inf') else ret

    def bfs(self, start_i, start_j, distance, grid, buildings):
        n, m = len(grid), len(grid[0])
        queue = [(start_i, start_j, 0)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[start_i][start_j] = True
        can_reach_count = 0
        while queue:
            i, j, dist = queue.pop()
            # A good pruning is while doing BFS, also 
            # visit points with 1 but not put in queue
            # Then check at the end to make sure it can reach all other buildings
            for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= x < n and 0 <= y < m and not visited[x][y]:
                    visited[x][y] = True
                    if grid[x][y] == 0:
                        distance[(x, y)].append(dist+1)
                        queue.insert(0, (x, y, dist+1))
                    elif grid[x][y] == 1:
                        can_reach_count += 1    
        return can_reach_count == buildings - 1  