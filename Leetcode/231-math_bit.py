class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        return n & (-n) == n

class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n-1) == 0