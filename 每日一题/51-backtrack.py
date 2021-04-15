class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:        
        def backtrack(row):
            if row == n:
                res.append(list(board))
            for col in range(n):
                # if satisfied:
                if col not in cols and col-row not in diag and col+row not in off_diag:
                    cols.add(col)
                    diag.add(col - row)
                    off_diag.add(col + row)
                    board.append("."*(col) + "Q" + "."*(n-col-1))
                    
                    # move to next row
                    backtrack(row+1)
                    
                    # back track
                    board.pop()
                    off_diag.remove(col+row)
                    diag.remove(col-row)
                    cols.remove(col)
        res = []
        board = []
        cols = set()
        diag = set()
        off_diag = set()

        backtrack(0)
        return res