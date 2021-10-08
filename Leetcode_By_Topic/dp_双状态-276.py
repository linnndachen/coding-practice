class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return k

        # case 1 = n is 1, case 2 = n is 2
        case1, case2 = k, k * k

        for i in range(n - 2):
            case1, case2 = case2, (case1 + case2) * (k - 1)

        return case2
