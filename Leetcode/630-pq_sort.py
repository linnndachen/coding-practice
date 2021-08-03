import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort by end time, pioritize by duration
        courses.sort(key=lambda x: x[1])

        heap, time = [], 0
        for t, end in courses:
            time += t
            heapq.heappush(heap, -t)

            if time > end:
                time += heapq.heappop(heap)

        return len(heap)

    """
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort by end time, pioritize by duration
        courses.sort(key=lambda x: x[1])

        res, heap = 0, []
        days, i = 0, 0

        while i < len(courses):
            time, end = courses[i][0], courses[i][1]

            if end > days or not heap:
                heapq.heappush(heap, (end, time))
                i += 1

            e, d = heapq.heappop(heap)
            if d + days <= e:
                res += 1
                days += d

            # remove the ones impossible to attend
            while heap and heap[0] < day:
                heapq.heappop(heapq)

        return res
    """