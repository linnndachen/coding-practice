"""
class Node:
    def __init__(self,start,end):
        self.end = end
        self.start = start
        self.left = None
        self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar:
    def __init__(self):
        self.root = None
    
    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))

"""
import bisect
class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False

        i = bisect.bisect_right(self.calendar, start)
        if i % 2 != 0:
            return False

        j = bisect.bisect_left(self.calendar, end)
        if i != j:
            return False

        self.calendar[i:i] = [start, end]
        return True
"""
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s1, e1 in self.calendar:
            # if max(s1, start) < min(e1, end)
            if start < e1 and s1 < end:
                return False
        self.calendar.append([start, end])
        return True
"""


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)