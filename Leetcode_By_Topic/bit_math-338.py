from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)

        for i in range(1, n+1):
            # countBits(all bits of num except the last bit) 
            # + countBits(the last bit)

            # if it was a even num - ending in 0 bit
            if (i&1) == 0:
                # the last bit can be ignore
                res[i] = res[i>>1]
            else:
                # if it was odd, the previous 1's we have + the new one
                res[i] = res[i>>1] + 1
        return res