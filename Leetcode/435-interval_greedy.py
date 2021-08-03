class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res, end = 0, float('-inf')
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                res += 1
        return res