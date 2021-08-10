
import heapq
from typing import List
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # [start, duration]
        # process - shortest processing time, then smallest index
        sorted_task = sorted([(start, duration, idx) for idx, (start, duration) in enumerate(tasks)])

        heap, res, last = [], [], 0

        for start, duration, idx in sorted_task:
            while heap and last < start:
                cost, i, s = heapq.heappop(heap)
                last = max(s, last) + cost
                res.append(i)

            heapq.heappush(heap, (duration, idx, start))

        while heap:
            res.append(heapq.heappop(heap)[1])

        return res