class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        We need to check two things:
        1) the external corners must appear only once. 
        (The ones inside have to be an even number - 2/4: we filter them with xor)
        2) sum (all the rectangles areas) == the area created by the external corners
        """

        corners = set()
        area = 0
        for left_x, low_y, right_x, high_y in rectangles:
            bottom_left = (left_x, low_y)
            top_left = (left_x, high_y)
            bottom_right = (right_x, low_y)
            top_right = (right_x, high_y)

            area += (right_x - left_x) * (high_y - low_y)

            for i in [top_left, top_right, bottom_left, bottom_right]:
                if i not in corners:
                    corners.add(i)
                else:
                    corners.remove(i)

        if len(corners) != 4:
            return False

        corners = sorted(corners)
        first = corners.pop(0)
        last = corners.pop()
        return area == (last[0] - first[0]) * (last[1] - first[1])

        """
        # more concise
        area = 0
        corners = set()
        get_area = lambda: (Y-y) * (X-x)

        for x, y, X, Y in rectangles:
            area += get_area()
            corners ^= {(x,y), (x,Y), (X,y), (X,Y)}

        if len(corners) != 4: 
            return False

        x, y = min(corners, key=lambda x: x[0] + x[1])
        X, Y = max(corners, key=lambda x: x[0] + x[1])
        return get_area() == area
        """