import random
import bisect
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weighted = []
        self.total = 0
        for a, b, x, y in rects:
            # remember to +1 here
            self.total += (x-a+1) * (y-b+1)
            self.weighted.append(self.total)

    def pick(self) -> List[int]:
        pick = random.random() * self.total
        idx = bisect.bisect(self.weighted, pick)

        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
