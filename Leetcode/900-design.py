import bisect
from typing import List

class RLEIterator:
    # [8,8,8,5,5]
    def __init__(self, encoding: List[int]):
        self.indexes = []
        self.vals = []
        self.cur_n = 0
        cur, i = 0, 0

        while i < len(encoding):
            if encoding[i] != 0:
                cur += encoding[i]
                self.indexes.append(cur)
                self.vals.append(encoding[i+1])

            i += 2

    def next(self, n: int) -> int:
        self.cur_n += n

        if not self.indexes:
            return -1

        idx = bisect.bisect_left(self.indexes, self.cur_n)

        if idx == len(self.indexes):
            return -1

        return self.vals[idx]


    """
    # [8,8,8,5,5]
    def __init__(self, encoding: List[int]):
        self.data = encoding
        self.index = 0


    def next(self, n: int) -> int:
        while self.index < len(self.data):
            if n <= self.data[self.index]:
                self.data[self.index] -= n
                return self.data[self.index + 1]

            n -= self.data[self.index]
            self.index += 2

        return -1
    """