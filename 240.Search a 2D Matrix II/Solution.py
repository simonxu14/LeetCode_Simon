__author__ = 'Simon'
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # index = 0
        # if len(matrix) == 0:
        #     return index == 1
        # row = len(matrix)
        # column = len(matrix[0])
        # for i in range(column):
        #     if target == matrix[0][i]:
        #         index = 1
        #     if target > matrix[0][i] and target < matrix[0][i+1]:
        #         for j in range(1, row):
        #             if target == matrix[j][i]:
        #                 index = 1
        #     if i == column - 1:
        #         for j in range(1, row):
        #             if target == matrix[j][i]:
        #                 index = 1
        # return index == 1
        row = len(matrix)
        column = len(matrix[0])
        m = 0
        n = column - 1
        while m < row and n >= 0:
            if matrix[m][n] == target:
                return True
            if matrix[m][n] > target:
                n -= 1
            if matrix[m][n] < target:
                m += 1
        return False
