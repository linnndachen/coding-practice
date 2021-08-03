from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), \
                      (-1, 0), (-1, 1), (0, 1), (1, 1)]

        m, n = len(board), len(board[0])

        for x in range(m):
            for y in range(n):
                cnt_live = 0

                for dx, dy in directions:
                    nx, ny = x+dx, y+dy

                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue

                    if abs(board[nx][ny]) == 1:
                        cnt_live += 1

                if board[x][y] == 1 and (cnt_live < 2 or \
                                           cnt_live > 3):
                    board[x][y] = -1

                if board[x][y] == 0 and cnt_live == 3:
                    board[x][y] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0