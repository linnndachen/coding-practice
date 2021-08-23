class Solution:
    def getSum(self, a: int, b: int) -> int:
        # using XOR
        x, y = abs(a), abs(b)

        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        # if a && b have the same sign
        if a*b >= 0:
            # sum of two positive int
            while y: # y is the carry
                x, y = x ^ y, (x & y) << 1
        else:
            # diff of the two positive int
            while y: # y is the borrow
                x, y = x ^ y, ((~x) & y) << 1

        return x * sign

    """
    def getSum(self, a: int, b: int) -> int:
        # langauge specific
        # 32 bit mask in hexadecimal
        mask = 0xffffffff

        # works both as while loop and single value check 
        while (b & mask) > 0:

            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry

        # handles overflow
        return (a & mask) if b > 0 else a
    """