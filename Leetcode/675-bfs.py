class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # Time - O(mn) * O(mn)
        # Space - (Omn)

        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)

        sr = sc = ans = 0 # source row, source col
        for _, tr, tc in trees: # target row, target col
            d = self.astar(forest, sr, sc, tr, tc)
            if d < 0: 
                return -1
            ans += d
            sr, sc = tr, tc

        return ans

    def astar(self, forest, sr, sc, tr, tc):
        m, n = len(forest), len(forest[0])
        heap = [(0, 0, sr, sc)] # f:actual dis + guess dis, g:actual dis
        cost = {(sr, sc): 0}
        while heap:
            f, g, r, c = heapq.heappop(heap)
            if r == tr and c == tc: 
                return g
            for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if 0 <= nr < m and 0 <= nc < n and forest[nr][nc]:
                    ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                    if ncost < cost.get((nr, nc), 9999):
                        cost[nr, nc] = ncost
                        heapq.heappush(heap, (ncost, g+1, nr, nc))
        return -1
    
    """
    def bfs(self, forest, sr, sc, tr, tc):
        m, n = len(forest), len(forest[0])

        queue = deque([(sr, sc, 0)]) # i , j, steps
        seen = set((sr, sc))
        while queue:
            i, j, steps = queue.popleft()
            
            if i == tr and j == tc:
                return steps

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i, j
                if 0 <= x+dx < m and 0 <= y+dy < n and forest[x+dx][y+dy] != 0:
                    x, y = dx+x, dy+y
                if (x, y) not in seen:
                    seen.add((x, y))
                    queue.append((x, y, steps+1))

        return -1
        """