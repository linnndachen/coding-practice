class Solution:
    def totalNQueens(self, n: int) -> int:

        self.res = 0
        self.dfs([-1] * n, 0)
        return self.res

    def dfs(self, nums, pos):
        if pos == len(nums):
            self.res += 1
            return

        for i in range(len(nums)):
            nums[pos] = i
            if self.valid(nums, pos):
                self.dfs(nums, pos + 1)

    def valid(self, nums, pos):
        for i in range(pos):
            if nums[pos] == nums[i] or abs(nums[pos] - nums[i]) == abs(pos - i):
                return False
        return True

class SolutionII:
    def totalNQueens(self, n: int) -> int:
        diag1, diag2, past_cols = set(), set(), set()

        def backtrack(row):
            if row == n:
                return 1

            count = 0

            for col in range(n):
                if row+col in diag1 or row-col in diag2 or col in past_cols:
                    continue
                diag1.add(row+col)
                diag2.add(row-col)
                past_cols.add(col)

                count += backtrack(row + 1)

                diag1.remove(row+col)
                diag2.remove(row-col)
                past_cols.remove(col)
            return count

        return backtrack(0)