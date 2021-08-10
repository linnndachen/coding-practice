class CustomStack:
    def __init__(self, maxSize: int):
        self.size = maxSize
        # stack = [(val, delta), (val, delta)]
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append([x, 0])

    def pop(self) -> int:
        if not self.stack:
            return -1

        res, inc = self.stack.pop()
        res += inc

        if self.stack:
            self.stack[-1][1] += inc

        return res
        
    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.stack[min(k, len(self.stack)) - 1][1] += val
    """
    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        # inc[i] is the change needed for all(stack[0] ~ stack[i])
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: 
            return -1

        # transfer the delta requirement to the one before
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]

        # pop the element +/- the necessary change = updated
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val
    """
    """
    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
 
    def push(self, x: int) -> None:
        if self.size > 0:
            self.stack.append(x)
            self.size -= 1
    def pop(self) -> int:
        if self.stack:
            data = self.stack.pop()
            self.size += 1
            return data

        return -1

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            k = len(self.stack)

        for i in range(k):
            self.stack[i] += val
    """