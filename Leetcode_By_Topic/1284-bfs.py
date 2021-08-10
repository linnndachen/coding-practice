class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = 0
        for i in range(m):
            for j in range(n):
                start += mat[i][j] << (i * n + j)

        queue = collections.deque([(start, 0)])
        visited = set([start])

        while queue:
            state, steps = queue.popleft()
            if state == 0:
                return steps
            for i in range(m):
                for j in range(n):
                    new_state = state
                    # flip part
                    for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                        if m > r >= 0 <= c < n:
                            new_state ^= 1 << (r * n + c)
                    
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))
        return -1

        """
        def filp(self, start, i, j):
            # we also include 0, 0 because we need to flip ourself as well
            for dx, dy in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + dx
                y = j + dy

                # a string problem 
                if 0 <= x < m and 0 <= y < n:
                    # print(i, j, x, y) 
                    # (i * n + j) is turning this into "0000", "0001"
                    # store all possible combination as bitmask
                    start ^= (1 << (x * n + y))

            return start
        """