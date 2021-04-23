"""
state[i][i] = 1;
state[i][i + 1] = 1 if s[i] == s[i + 1]
state[i][i + 1] = 2 if s[i] != s[i + 1]
state[i][j] = min(state[i][k] + state[k + 1][j]) for i <= k <= j - 1
** if s[i] equals to s[j] , state[i][j] should -1
"""
class Solution:
    def strangePrinter(self, s: str) -> int:
        self.memo = {}
        s = re.sub(r'(.)\1*', r'\1', s)
        return self.dfs(s, 0, len(s)-1)

    def dfs(self, s, left, right):
        if left > right:
            return 0

        if (left, right) in self.memo:
            return self.memo[(left, right)]

        # add the cost of the current one
        res = self.dfs(s, left+1, right) + 1

        for k in range(left+1, right+1):
            if s[k] == s[left]:
                # then we can skip the cost of k
                res = min(res, self.dfs(s, left, k-1) + self.dfs(s, k+1, right))

        self.memo[(left, right)] = res

        return res