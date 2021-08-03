class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        covered, end = 0, float("-inf")
        for _, e in intervals:
            if e <= end:
                covered += 1
            else:
                end = e

        return len(intervals) - covered