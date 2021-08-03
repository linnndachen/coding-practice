class Solution:
    # template version
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        d = collections.defaultdict(int)
        res = 0
        
        for s, e in intervals:
            d[s] += 1
            d[e] -= 1
        
        for time in sorted(d.keys()):
            res += d[time]
            
            if res > 1:
                return False
        
        return True

    """
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True

        intervals.sort(key=lambda x: x[0])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
    """