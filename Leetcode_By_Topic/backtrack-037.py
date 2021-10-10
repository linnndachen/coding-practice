from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)
                    
    def backtrack(self, board, r, c):
        
        # Go to next empty space
        while board[r][c] != '.':
            c += 1
            
            if c == 9: 
                c, r = 0, r+1
            
            if r == 9: # base case
                return True
            
        # for all possibilities,
        for i in range(1, 10):
            # if one of them works
            if self.isValidSudokuMove(board, r, c, str(i)):
                board[r][c] = str(i)
                
                #continue to test if it will fit the rest
                if self.backtrack(board, r, c):
                    return True
                
                # backtracking if it doesn't work and continue
                # with another possibility
                board[r][c] = '.'
                
        return False
    
    def isValidSudokuMove(self, board, r, c, n):
        # Check row
        if any(board[r][j] == n for j in range(9)):
            return False
        
        # Check col
        if any(board[i][c] == n for i in range(9)):
            return False
        
        # Check block
        br, bc = 3*(r//3), 3*(c//3)
        if any(board[i][j] == n for i in range(br, br+3) for j in range(bc, bc+3)):
            return False
        
        return True

        
        