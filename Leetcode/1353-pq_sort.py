from typing import List
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # key idea - sort by start time and pq by end time

        events.sort(reverse=True)
        pq = []
        res = day = 0

        while events or pq:
            if not pq:
                day = events[-1][0]

            # push all the events that we can attend by this day
            while events and events[-1][0] <= day:
                heapq.heappush(pq, events.pop()[1])

            heapq.heappop(pq)
            res += 1
            day += 1

            # remove the ones impossible to attend
            while pq and pq[0] < day:
                heapq.heappop(pq)

        return res