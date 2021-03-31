import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1, 2, 2, 3 = 8
        # if h == len(piles), ans = max(piles)
        # if h > len(piles), ans < max(piles)
        # thus, range = [1, max(piles)]

        # if Koko can eat all bananas in H hours with eating speed m
        def is_possible(m):
            # Math.ceil(p/m) = ((p-1) // m) + 1
            return sum(math.ceil(p/m) for p in piles) <= h


        low, hi = 1, max(piles)
        while low < hi:
            mid = (low + hi) // 2
            if not is_possible(mid):
                low = mid + 1
            else:
                hi = mid
        return low875-binary.py