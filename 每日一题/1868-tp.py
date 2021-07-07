from typing import List
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        i, j = 0, 0

        res = []

        while i < len(encoded1) and j < len(encoded2):
            cnt1, cnt2 = encoded1[i][1], encoded2[j][1]
            val1, val2 = encoded1[i][0], encoded2[j][0]

            n = val1 * val2
            freq = min(cnt1, cnt2)

            encoded1[i][1] -= freq
            encoded2[j][1] -= freq

            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1

            if not res or res[-1][0] != n:
                res.append([n, freq])
            else:
                res[-1][1] += freq

        return res