class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)

        sr = sc = ans = 0 # source row, source col
        for _, tr, tc in trees: # target row, target col
            d = self.bfs(forest, sr, sc, tr, tc)
            if d < 0: 
                return -1
            ans += d
            sr, sc = tr, tc

        return ans

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