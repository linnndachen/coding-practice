class SnapshotArray:
    # to advoid making a copy every time, we can only record the change
    def __init__(self, n):
        self.data = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.data[index].append([self.snap_id, val])
        print(self.data)

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.data[index], [snap_id + 1]) - 1
        print(i)
        return self.data[index][i][1]
    """
    # for self.data, if I use [] instead of {}, it will TLE
    # the drawback of this design is that I need to make a copy of self.data every time I take
    # a snap. This could be unnecessary since only minor change might happed or exactly same copy

    def __init__(self, length: int):
        self.data = {}
        self.snap_id = -1
        self.snaps = collections.defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.data[index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.snaps[self.snap_id] = self.data.copy()
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.snaps:
            data = self.snaps[snap_id]
            if index in data:
                return data[index]
        return 0
    """