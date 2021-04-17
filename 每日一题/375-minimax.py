class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # starting point is 0, because if we only had 1 as n
        # we don't even need to guess
        need = [[0] * (n+1) for _ in range(n+1)]

        # search range, 1 to n-1
        for lo in range(n, 0, -1):
            # starting point, 2 to n
            for hi in range(lo+1, n+1):
                need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
                                   for x in range(lo, hi))

        return need[1][n]


# 1 2 3 4 5
# x (choice): left vs right area
# 1: 1 + max([0], [2,3,4,5])
# 2: 2 + max([1], [3 4 5])
# 3: 3 + max([1 2], [4 5])
# 4: 4 + ([1 2 3], [5])
# 5: 5 + ([1 2 3 4], [0])
# we pick the largest area - if we pick x, the wrost case we need to pay
# then, inside the larger area, we pick the smallest amount