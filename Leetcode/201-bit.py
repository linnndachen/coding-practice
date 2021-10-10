class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0

        # find the common prefix
        # while loop until they are equal
        while m < n:
            m = m >> 1
            n = n >> 1

            shift += 1

        return m << shift