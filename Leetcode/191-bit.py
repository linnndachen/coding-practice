class Solution:
    def hammingWeight(self, n: int) -> int:
        res, power = 0, 31

        while n:
            res += (n & 1)
            # right shift n
            n = n >> 1
            power -= 1

        return res