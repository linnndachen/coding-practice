from typing import List
class Excel:

    def __init__(self, H: int, W: str):
        # print(ord("A"), ord("a"), ord("Z"), ord("z"))
        self.height = H
        self.width = ord(W) - ord("A") + 1

        self.matrix = [[0] * self.width for _ in range(self.height)]

    def set(self, r: int, c: str, v: int) -> None:
        if r - 1 >= self.height or (ord(c) - ord("A")) >= self.width:
            return

        self.matrix[r-1][ord(c) - ord("A")] = v

    def get(self, r: int, c: str) -> int:
        if (r - 1) >= self.height or (ord(c) - ord("A")) >= self.width:
            return 0

        v = self.matrix[r-1][ord(c) - ord("A")]
        if type(v) is int:
            return v
        return self.calculate(v)


    def sum(self, r: int, c: str, strs: List[str]) -> int:
        if (r - 1) >= self.height or (ord(c) - ord("A")) >= self.width:
            return 0

        self.matrix[r-1][ord(c) - ord("A")] = strs
        return self.calculate(strs)

    def calculate(self, strs):
        total = 0
        for v in strs:
            if ":" in v:
                start, end = v.split(":")
                for i in range(int(start[1:]), int(end[1:])+1):
                    for j in range(ord(start[0])-ord("A"), \
                                   ord(end[0])-ord("A")+1):
                        val = self.matrix[i-1][j]
                        if type(val) == int:
                            total += val
                        else:
                            total += self.calculate(val)
            else:
                val = self.matrix[int(v[1:])-1][ord(v[0])-ord("A")]

                if type(val) == int:
                    total += val
                else:
                    total += self.calculate(val)
        return total