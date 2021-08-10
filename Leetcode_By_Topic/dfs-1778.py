# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
class GridMaster(object):
   def canMove(self, direction: str) -> bool:
       pass

   def move(self, direction: str) -> bool:
       pass

   def isTarget(self) -> None:
       pass

from collections import deque
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        # first use dfs to find all possible reachable positions
        dirs = {"U":(-1, 0), "D":(1, 0), "L":(0, -1), "R":(0, 1)}
        anti = {"U":"D", "D":"U", "L":"R", "R":"L"}

        valid_pos = {}
        valid_pos[(0, 0)] = master.isTarget()

        def _dfs(x, y):
            for d in dirs:
                dx, dy = dirs[d]
                nx, ny = x + dx, y + dy
                if (nx, ny) not in valid_pos and master.canMove(d):
                    # move forward
                    master.move(d)
                    valid_pos[(nx, ny)] = master.isTarget()
                    _dfs(nx, ny)
                    # move back
                    master.move(anti[d])

        _dfs(0, 0)

        queue = deque([(0, 0, 0)])
        seen = set()
        while queue:
            x, y, steps = queue.popleft()

            if valid_pos[(x, y)] == True:
                return steps

            for dx, dy in dirs.values():
                nx, ny = dx+x, dy+y

                if (nx, ny) in valid_pos and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

        return -1