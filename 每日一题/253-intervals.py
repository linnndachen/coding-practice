class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        start = sorted([x for x, y in intervals])
        end = sorted([y for x, y in intervals])
        
        # res - occupied room
        # e - earliest available time index
        e, res = 0, 0
        
        for i in range(len(start)):
            if start[i] < end[e]:
                res += 1
            else:
                e += 1
        
        return res