from typing import List
from collections import deque

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        table = {e.id: e for e in employees}

        res, queue = 0, deque([table[id]])

        while queue:
            child = queue.popleft()
            res += child.importance
            queue.extend([table[child_id] for child_id in child.subordinates])

        return res