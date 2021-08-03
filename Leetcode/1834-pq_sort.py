from typing import List
from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(start, duration, idx) for idx, (start, duration) in enumerate(tasks)]
        tasks.sort()
        
        res, pq = [], []
        i, end = 0, 0

        while len(res) < len(tasks):
            # Push all the tasks available at current CPU clock
            while i < len(tasks) and tasks[i][0] <= end:
                heappush(pq, (tasks[i][1], tasks[i][2]))
                i += 1

            if pq:
                ptime, index = heappop(pq)
                res.append(index)
                end += ptime
            else:
                # Jump to the next available task
                end = tasks[i][0]
        return res

    """
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

    """