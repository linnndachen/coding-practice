from collections import defaultdict
from typing import List
class Solution:
    # dfs
    # cannot use bfs, bfs does not return a global minimum solution
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = collections.defaultdict(int)

        for t in transactions:
            m[t[0]] -= t[2]
            m[t[1]] += t[2]
        debt = [d for d in m.values()]

        def dfs(idx):
            n = len(debt)
            while idx < n and debt[idx] == 0:
                idx += 1

            if idx == n:
                return 0

            res = float('inf')
            for j in range(idx+1, n):
                if debt[j] * debt[idx] < 0:

                    debt[j] += debt[idx]
                    res = min(res, 1+dfs(idx+1))
                    # backtrack
                    debt[j] -= debt[idx]

            return res

        return dfs(0)