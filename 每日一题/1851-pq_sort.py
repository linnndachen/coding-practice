from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort by starting time, 满足条件的按照 interval len 来排

        sortedQ = sorted([(n, i) for i, n in enumerate(queries)])
        intervals.sort()

        res, heap = [-1 for _ in range(len(queries))], []
        i = 0

        for query, curJ in sortedQ:
            while i < len(intervals) and intervals[i][0] <= query:
                d = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (d, intervals[i][1]))
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                res[curJ] = heap[0][0]

        return res