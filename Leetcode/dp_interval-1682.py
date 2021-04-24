class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.memo = {}
        return self.dfs(s, 0, len(s)-1, "#")


    def dfs(self, s, left, right, prev):
        if left >= right:
            return 0

        if (left, right, prev) in self.memo:
            return self.memo[(left, right, prev)]

        if s[left] == s[right] and s[left] != prev:
            self.memo[(left, right, prev)] = 2 + self.dfs(s, left+1, right-1, s[left])
        else:
            self.memo[(left, right, prev)] = max(self.dfs(s, left+1, right, prev), \
                                      self.dfs(s, left, right-1, prev))
        return self.memo[(left, right, prev)]