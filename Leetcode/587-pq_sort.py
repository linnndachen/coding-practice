from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # 这道题的twist是需要知道 Monotone_Chain_Convex_Hull 这个知识点
        # 但是有用的地方是，用两数相乘的办法找到同个 x，哪个最大/最小
        def is_clockwise(p0, p1, p2) -> bool:
            """
            Determine the orientation the slope p0p2 is on the clockwise
            orientation of the slope p0p1.
            """
            return (p1[1] - p0[1]) * (p2[0] - p0[0]) > \
                (p2[1] - p0[1]) * (p1[0] - p0[0])

        sortedPoints = sorted(trees)

        # Scan from left to right to generate the lower part of the hull.
        hull = []
        for p in sortedPoints:
            while len(hull) > 1 and is_clockwise(hull[-2], hull[-1], p):
                hull.pop()

            hull.append(p)

        if len(hull) == len(trees):
            return hull

        # Scan from right to left to generate the higher part of the hull.
        # Remove the last point first as it will be scanned again.
        hull.pop()
        for p in reversed(sortedPoints):
            while len(hull) > 1 and is_clockwise(hull[-2], hull[-1], p):
                hull.pop()

            hull.append(p)

        # Pop the first point as it is already added to hull when processing
        # the lower part.
        hull.pop()

        return hull