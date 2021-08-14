from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # O((N−L)L)
        windowSize, n = 10, len(s)
        seen, res = set(), set()

        for start in range(n-windowSize+1):
            tmp = s[start:start+windowSize]
            if tmp in seen:
                res.add(tmp[:])

            seen.add(tmp)

        return res

"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # rolling hash - O(N-L)*2
        windowSize, n = 10, len(s)

        if n <= windowSize:
            return []

        base = 4
        # 4^10, 变为4进制
        powerBaseL = pow(base, windowSize)

        Atoi = {"A":0, "C":1, "G":2, "T":3}
        nums = [Atoi.get(char) for char in s]

        seen, res = set(), set()
        pattern = 0
        for start in range(n-windowSize+1):
            if start != 0:
                # - the first element and + the tail element
                pattern = pattern*base - nums[start-1]*powerBaseL + \
                            nums[start+windowSize-1]
            else:
                for i in range(windowSize):
                    pattern = pattern*base + nums[i]

            if pattern in seen:
                res.add(s[start:start+windowSize])

            seen.add(pattern)

        return res
"""