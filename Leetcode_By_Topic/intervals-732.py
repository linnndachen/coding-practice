import heapq
class MyCalendarThree:
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
    
    """
    #  Lines Segment Tree method o(1)
    def __init__(self):
        self.seg = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)
        

    def book(self, start: int, end: int) -> int:
        def update(s, e, l = 0, r = 10**9, ID = 1):
            if r <= s or e <= l: 
                return
            
            if s <= l < r <= e:
                self.seg[ID] += 1
                self.lazy[ID] += 1
                
            else:
                m = (l + r) // 2
                update(s, e, l, m, 2 * ID)
                update(s, e, m, r, 2 * ID + 1)
                self.seg[ID] = self.lazy[ID] + max(self.seg[2 * ID], self.seg[2 * ID+1])
                
        update(start, end)
        
        return self.seg[1]
        """
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)