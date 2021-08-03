import heapq, collections
class MyCalendarThree:
    def __init__(self):
        self.seg = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)


    def book(self, start: int, end: int) -> int:
        def update(s2, e2, start = 0, end = 10**9, dep = 1):
            # no overlaps
            if s2 >= end or start >= e2:
                return

            # completely covers the original range
            if s2 <= start < end <= e2:
                self.seg[dep] += 1
                # lazy acts like storing the parent node
                self.lazy[dep] += 1

            else: # partially cover
                m = (start + end) // 2
                update(s2, e2, start, m, 2 * dep) # left node
                update(s2, e2, m, end, 2 * dep + 1) # right node
                self.seg[dep] = self.lazy[dep] + max(self.seg[2 * dep], self.seg[2 * dep+1])
                # print(self.seg, dep)
                # print(self.lazy)

        update(start, end)

        return self.seg[1]

    """
    def __init__(self):
        self.delta = collections.Counter()

    def book(self, s, e):
        self.delta[s] += 1
        self.delta[e] -= 1

        cur = res = 0

        for x in sorted(self.delta):
            cur += self.delta[x]
            res = max(cur, res)

        return res
    """

    """
    O - N^2 Log n
    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> int:
        self.books.append([start, end])
        self.books = sorted(self.books, key = lambda x: x[0])

        heap =[]
        # first ending time
        heapq.heappush(heap, self.books[0][1])

        # sweep the line and compare
        for i in range(1, len(self.books)):
            if self.books[i][0] >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, self.books[i][1])
            else:
                heapq.heappush(heap, self.books[i][1])
        return len(heap)
    """