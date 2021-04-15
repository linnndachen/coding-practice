class Solution:
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