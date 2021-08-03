from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def _convertPos(num):
            # 1: [m-1, 0]
            r, c = divmod(num-1, n)

            if r % 2 == 0: # 13(12) -> [2, 0]
                return n-1-r, c

            return n-1-r, n-1-c # 12(11) -> [1, 5]

        queue = deque()
        queue.append((0, 1))
        seen = set()
        seen.add(1)

        while queue:
            steps, pos = queue.popleft()
            x, y = _convertPos(pos)

            if board[x][y] != -1:
                pos = board[x][y]

            # flag: pay attention to where you put this if statement
            # if we put before board[x][y] != -1, then we will have
            # additional 1 step
            if pos == n*n:
                return steps

            for dx in range(1, 7):
                new_pos = pos + dx

                if new_pos <= n*n and new_pos not in seen:
                    queue.append((steps+1, new_pos))
                    seen.add(new_pos)
        return -1