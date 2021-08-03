class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31

        while n:
            # left shift result by 1 bit
            # then, if the last bit of n is 1, make res 1
            res += (n & 1) << power
            # right shift n
            n = n >> 1
            power -= 1

        return res

    def reverseBits1(self, n):
        """
        this is more optimized than the above soltuion, because we get the answer
        in 5 steps. The previous solution get it in 31 steps. 
        0xff00ff00 is hex number, range from 1 - 15
        """
        # basically, swapping the first halp and the second half
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n