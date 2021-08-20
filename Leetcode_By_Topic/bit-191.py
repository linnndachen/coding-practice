class Solution1:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1

        return cnt

class Solution2:
    def hammingWeight(self, n: int) -> int:
        res, power = 0, 31

        while n:
            res += (n & 1)
            n = n >> 1
            power -= 1

        return res


class Solution3:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
