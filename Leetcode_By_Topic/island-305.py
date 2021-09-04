from typing import List


class UF:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
        self.count = 0

    def add(self, x, y):
        if (x, y) not in self.parents:
            self.parents[(x, y)] = (x, y)
            self.ranks[(x, y)] = 1
            self.count += 1

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
            p = self.parents[p]
        return p

    def union(self, p, q):
        p1, p2 = self.find(p), self.find(q)

        if p1 != p2:
            if self.ranks[p1] > self.ranks[p2]:
                self.parents[p2] = p1
            elif self.ranks[p1] < self.ranks[p2]:
                self.parents[p1] = p2
            else:
                self.parents[p1] = p2
                self.ranks[p2] += 1

            self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UF()
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in positions:
            uf.add(x, y)

            for dx, dy in directions:
                nx = dx + x
                ny = dy + y

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                if (nx, ny) in uf.parents:
                    uf.union((x, y), (nx, ny))

            res.append(uf.count)

        return res
