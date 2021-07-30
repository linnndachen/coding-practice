from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))

        if w < projects[0][0]:
            return 0

        i, heap = 0, []
        cnt = 0
        for _ in range(min(k, len(projects))):
            while i < len(profits) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1

            if not heap:
                break

            w += (-heapq.heappop(heap))

        return w