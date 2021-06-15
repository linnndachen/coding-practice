import bisect
class MyCalendarTwo:
    # same time complexity but with cleaner code
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        bisect.insort(self.calendar, (start, 1))
        bisect.insort(self.calendar, (end, -1))

        bookings = 0
        for time, freq in self.calendar:
            # iterate through the the calender
            bookings += freq
            if bookings == 3:
                self.calendar.pop(bisect.bisect_left(self.calendar, (start, 1)))
                self.calendar.pop(bisect.bisect_left(self.calendar, (end, -1)))
                return False

        return True
"""
class MyCalendarTwo:
    # O N^2 - most straight forward answer
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s1, e1 in self.overlaps:
            if start < e1 and s1 < end:
                return False
        for s1, e1 in self.calendar:
            if start < e1 and s1 < end:
                self.overlaps.append(max(start, s1), min(end, e1))

        self.calendar.append((start, end))

        return True

"""


class MyCalendarTwo:
    def __init__(self):
        self.pos = []
        self.cnt = {}

    def book(self, start: 'int', end: 'int') -> 'bool':
        # log n to find
        i = bisect.bisect_left(self.pos, start)
        j = bisect.bisect_left(self.pos, end)
        # wrost case is N
        if any(self.cnt[self.pos[k]] >= 2 for k in range(i, j)):
            return False

        # update the overlaps
        if start not in self.cnt:
            c = self.cnt[self.pos[i-1]] if i-1 >= 0 else 0
            if c >= 2: 
                return False
            # insert On
            self.pos[i: i] = [start]
            j += 1
            self.cnt[start] = c

        if end not in self.cnt:
            self.pos[j: j] = [end]
            self.cnt[end] = self.cnt[self.pos[j-1]]

        for k in range(i, j):
            self.cnt[self.pos[k]] += 1
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)