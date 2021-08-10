class Solution:
    def __init__(self):
        self.seen = set()
        self.res = 0

    def maxUniqueSplit(self, s: str) -> int:
        self._dfs(0, 0, s)
        return self.res

    def _dfs(self, cur_idx, cnt, s):
        n = len(s)
        # boundary check
        if cur_idx == n:
            self.res = max(self.res, cnt)
            return
        # 剪枝
        if (cnt + n-cur_idx) <= self.res:
            return

        # backtrack
        for i in range(cur_idx, n):
            sub_s = s[cur_idx : cur_idx + (i-cur_idx+1)]
            if sub_s not in self.seen:
                self.seen.add(sub_s)
                self._dfs(i+1, cnt+1, s)
                self.seen.remove(sub_s)