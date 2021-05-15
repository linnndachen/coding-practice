class DisJointSet(object):
    # by value + index by array, not tuple
    def __init__(self):
        self.parents = {}
        self.count = 0
        self.forest = []

    def union(self, x, y):
        set1 = self.find(x)
        set2 = self.find(y)
        if set1 != set2:
            if self.forest[set1] < self.forest[set2]:
                    self.parents[set1] = set2
                    self.forest[set2] += self.forest[set1]
            else:
                self.parents[set2] = set1
                self.forest[set1] += self.forest[set2]
            self.count -= 1

    def find(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i

    def add(self, x):
        if self.parents.get(x): 
            return
        self.parents[x] = x
        self.count += 1

class Solution:
    def numIslands2(self, m, n, positions):
        uf = DisJointSet()
        uf.forest = [1] * (m*n)
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in positions:
            index = x * n + y
            uf.add(index)
            for i, j in directions:
                a, b = x + i, y + j
                if 0 <= a < m and 0 <= b < n and a * n + b in uf.parents:
                    uf.union(index, a * n + b)
            res.append(uf.count)
        return res


"""
# by rank
class DSU:
    def __init__(self):
        self.parents = {}
        self.rank = {}
        self.count = 0

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
            p = self.parents[p]

        return p

    def union(self, p, q):
        i, j = self.find(p), self.find(q)
        if i != j:
            if self.rank[i] > self.rank[j]:
                self.parents[j] = i
            elif self.rank[i] < self.rank[j]:
                self.parents[i] = j
            else:
                self.parents[i] = j
                self.rank[j] += 1

            self.count -= 1

    def add(self, p):
        if self.parents.get(p): 
            return

        self.parents[p] = p
        self.rank[p] = 0
        self.count += 1


class Solution:
    def numIslands2(self, m, n, positions):
        uf = DSU()
        res = []
        for x, y in positions:
            uf.add((x, y))
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dx = x + i
                dy = y + j
                if 0 <= dx < m and 0 <= dy < n and (dx, dy) in uf.parents:
                    uf.union((x, y), (dx, dy))
                    
            res.append(uf.count)
        return res
"""