from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)

        for i in range(1, n+1):
            # take the divide by 2 value and + if it was odd / even
            res[i] = res[i>>1] + (i&1)

        return res