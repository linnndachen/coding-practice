from typing import List
import random, bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prevSum = []
        self.total = 0
        for n in w:
            self.total += n
            self.prevSum.append(self.total)

    def pickIndex(self) -> int:
        pick = random.random() * self.total
        
        idx = bisect.bisect(self.prevSum, pick)

        return idx