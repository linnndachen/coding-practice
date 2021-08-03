class MinStack:
    def __init__(self):
        """
        # initialize your data structure here.
        """
        # stores the delta of time - cur_mini
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.mini = val

        delta = val - self.mini
        self.stack.append(delta)
        
        if delta < 0:
            self.mini = val
        
    def pop(self) -> None:
        # revert the new mini to old mini
        if self.stack[-1] < 0:
            self.mini = self.mini - self.stack[-1]

        return self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.stack[-1] + self.mini
        else:
            return self.mini

    def getMin(self) -> int:
        return self.mini
    """
    # 低配
    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini or val < self.mini[-1]:
            self.mini.append(val)
        else:
            self.mini.append(self.mini[-1])

    def pop(self) -> None:
        self.mini.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
    """

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()