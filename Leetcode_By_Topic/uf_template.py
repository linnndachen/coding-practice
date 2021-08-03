class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, i):
        """
        while i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
            i = self.parents[i]
        return i
        """
        root = i
        while self.parents[root] != root:
            root = self.parents[root]
        while self.parents[i] != root:
            parent = self.parents[i]
            self.parents[i] = root
            i = parent
        return root

    def union(self, p, q):
        root_p, root_q = map(self.find, (p, q))
        if root_p == root_q:
            return
        small, big = sorted([root_p, root_q], key=lambda x: self.sizes[x])
        self.parents[small] = big
        self.sizes[big] += self.sizes[small]

class UnionFindrank:
    # time - M + N ? 
    # Space: N
    def __init__(self, grid):
        self.parents = {}
        self.rank = {}
        row, col = len(grid), len(grid[0])
        self.counts = sum(grid[i][j] == "1" for i in range(row) for j in range(col))

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
            p = self.parents[p]

        return p


    def add(self, p):
        if p not in self.parents:
            self.parents[p] = p
            self.rank[p] = 1

    def union(self, p, q):
        # return parent node
        i, j = self.find(p), self.find(q)

        if i != j:
            if self.rank[i] > self.rank[j]:
                self.parents[j] = i
            elif self.rank[i] < self.rank[j]:
                self.parents[i] = j
            else:
                self.parents[i] = j
                self.rank[j] += 1

            self.counts -= 1

    def get_counts(self):
        return self.counts


"""
Rank is not the actual depth of the tree rather it is an upper bound. As such, on a find operation, the rank is allowed to get out of sync with the depth.
"""

