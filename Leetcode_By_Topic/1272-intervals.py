class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for x, y in intervals:
            remove_x, remove_y = toBeRemoved
            # original
            if y <= remove_x or x >= remove_y:
                res.append([x, y])

            # overlaps
            else:
                if x < remove_x:
                    res.append([x, remove_x])
                
                if y > remove_y:
                    res.append([remove_y, y])

        return res