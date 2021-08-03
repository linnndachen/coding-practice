from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def dfs(path, i):
            if i == n:
                res.append(path)
                return

            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    dfs(path + [s[i:j+1]], j+1)

        dfs([], 0)

        return res