class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # start with the gate and search the empty cells it can reach
        # then we take the smallest one
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))


        for x, y in queue:
            dist = rooms[x][y] + 1

            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < m and 0 <= new_y < n and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = dist
                    queue.append((new_x, new_y))