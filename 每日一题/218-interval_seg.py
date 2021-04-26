class Solution:
    def getSkyline(self, buildings):
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()
        # print(events)

        # res: result, [x, height]
        res = [[0, 0]]
        # [-height, ending position] so that we keep the current higgest point
        heap = [(0, float("inf"))]
        for start, negH, end in events:
            # 1, pop buildings that are already ended
            while heap[0][1] <= start: 
                heappop(heap)
            # 2, if it's the start-building event, make the building alive
            if negH:
                heappush(heap, (negH, end))
            # 3, if previous keypoint height != current highest height, edit the result
            if res[-1][1] != -heap[0][0]:
                res += [ [start, -heap[0][0]] ]
        return res[1:]


"""
import sortedcontainers
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        # to be a skyline point either:
        # 1. entering event with highest height
        # 2. leaving event with highest height
        # to handle edge case
        # sort the entering event by increasing order of height
        # sort the leaving event by decreasing order of height
        """
        # [[start, h, 1], [end, h, -1]....]
        events = [[x, b[2], enter] for b in buildings for x, enter in zip(b[:2], [1, -1])]

        events.sort(key=lambda x: (x[0], -x[1]*x[2]))
        ans = []
        # heights so far
        heights = sortedcontainers.SortedList()
        for i, event in enumerate(events):
            x, h, status = event[0], event[1], event[2]
            # when entering
            if status == 1:
                # if it is the first one or the higgest
                if not heights or h > heights[-1]:
                    ans.append([x,h])
                heights.add(h)
            else:
                heights.discard(h)
                if not heights:
                    ans.append([x, 0])
                elif h > heights[-1]:
                    ans.append([x, heights[-1]])
        return ans

"""