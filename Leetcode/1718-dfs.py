from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        N = n*2 -1
        res, used = [0]*N, [False] * (n+1)
        def _dfs(i):
            if i == N:
                return res

            if res[i]:
                return _dfs(i+1)

            for x in range(n, 0, -1):
                j = i if x ==1 else i+x

                if not used[x] and j < N and not res[j]:
                    res[i], res[j], used[x] = x, x, True

                    if _dfs(i+1):
                        return True

                    res[i], res[j], used[x] = 0, 0, False

            return False

        _dfs(0)
        return res