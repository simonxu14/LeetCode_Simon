__author__ = 'Simon'
class Solution(object):
    def check(self, board, start, choice):
        numbers = []
        for i in range (0, len(board)):
            num = board[start][i]
            if (choice== 'col'):
                num = board[i][start]
            if num != '.':
                num = int(num)
                if num < 0 or num > 9 or num in numbers:
                    return False
                numbers.append(num)
        return True

    def check_row(self, board, start):
        return self.check(board, start, 'row')

    def check_col(self, board, start):
        return self.check(board, start, 'col')

    def check_square(self, board, row, col):
        numbers = []
        for i in range(row, row+3):
            for j in range (col, col+3):
                print i, j
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    if num < 0 or num > 9 or num in numbers:
                        return False
                    numbers.append(num)
        return True

    def isValidSudoku(self, board):
            """
            :type board: List[List[str]]
            :rtype: bool
            """
            result = True
            for i in range (0, 9):
                result = result and self.check_row(board, i)
                result = result and self.check_col(board, i)
                if i % 3 == 0:
                    for j in range (0, 9):
                        if j % 3 == 0:
                            result = result and self.check_square(board, i, j)
            return result


    # def isValidSudoku(self, board):
    # """
    # :type board: List[List[str]]
    # :rtype: bool
    # """
    # big = set()
    # for i in xrange(0,9):
    #     for j in xrange(0,9):
    #         if board[i][j]!='.':
    #             cur = board[i][j]
    #             if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
    #                 return False
    #             big.add((i,cur))
    #             big.add((cur,j))
    #             big.add((i/3,j/3,cur))
    # return True