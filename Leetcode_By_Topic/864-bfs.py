# "." is empty, "#" is wall, "@" is starting point
# "a" is key and "A" is locks
# pick up the key and open the lock. Cannot walk over wall
# lowest num of moves to acquire all keys
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])

        all_keys = [0, 0, 0, 0, 0, 0]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    i_start, j_start = i, j
                elif grid[i][j].islower():
                    all_keys[ord(grid[i][j]) - ord('a')] = 1

        # turn to tuple so that we can hash it
        all_keys = tuple(all_keys)

        # BFS visit
        curr_queue = [(i_start, j_start, tuple(6 * [0]))]
        visited = {(i_start, j_start, tuple(6 * [0]))}
        moves = 0

        while curr_queue:
            next_queue = []
            for x, y, keys in curr_queue:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r, c = x + dx, y + dy
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != '#':

                        if grid[r][c] in '.@':
                            if (r, c, keys) not in visited:
                                visited.add((r, c, keys))
                                next_queue.append((r, c, keys))

                        # a new key
                        elif grid[r][c].islower():
                            new_keys = list(keys)
                            new_keys[ord(grid[r][c]) - ord('a')] = 1
                            new_keys = tuple(new_keys)
                            
                            if new_keys == all_keys:
                                return moves + 1
                            if (r, c, new_keys) not in visited:
                                visited.add((r, c, new_keys))
                                next_queue.append((r, c, new_keys))

                        else: # face a lock
                            # if we have the key
                            if keys[ord(grid[r][c].lower()) - ord('a')] == 1 and (r, c, keys) not in visited:
                                visited.add((r, c, keys))
                                next_queue.append((r, c, keys))
            curr_queue = next_queue
            moves += 1
        return -1