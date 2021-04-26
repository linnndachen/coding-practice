# equals to: the max # of intervals that are not overlapping
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        res, end = 0, float('-inf')
        for s, e in points:
            if s > end:
                res += 1
                end = e
        return res

# [[1,  6], [7,     12]]
#   [2,    8],   [10,     16]