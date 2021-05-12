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
