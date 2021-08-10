import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)-1 > hour:
            return -1

        low, high = 1, 10 ** 7 + 1
        n = len(dist)

        while low < high:
            mid = (high + low) // 2
            
            total_hours = 0
            for i, d in enumerate(dist):
                if i != n -1:
                    total_hours += math.ceil(d / mid)
                else:
                    total_hours += (d / mid)

            if total_hours > hour:
                low = mid + 1
            else:
                high = mid
        return low if low != 10 ** 7 + 1 else -1