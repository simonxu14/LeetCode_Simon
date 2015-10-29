__author__ = 'Simon'
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                self.update(board, m, n, i, j)
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

    def update(self, board, m, n, i, j):
        live = 0
        for p in range(max(i-1, 0), min(i+2, m)):
            for q in range(max(j-1, 0), min(j+2, n)):
                live += board[p][q] & 1
        if live == 3 or live == board[i][j] + 3:
            board[i][j] += 2