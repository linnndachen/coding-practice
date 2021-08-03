from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        return self.dfs(expression)

    def dfs(self, str1, memo={}):
        if str1.isdigit():
            return [int(str1)]

        if str1 in memo:
            return memo[str1]

        res = []
        for i, char in enumerate(str1):
            if char in "-+*":
                res1 = self.dfs(str1[:i])
                res2 = self.dfs(str1[i+1:])
                # key
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, char))

        memo[str1] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n