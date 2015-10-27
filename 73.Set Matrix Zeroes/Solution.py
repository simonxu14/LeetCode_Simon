__author__ = 'Simon'
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zero_row = []
        zero_col = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    # matrix[0][col] = 0
                    # matrix[row][0] = 0

                    if row not in zero_row:
                        zero_row.append(row)
                    if col not in zero_col:
                        zero_col.append(col)


        # for row in range(len(matrix)):
        #     if matrix[row][0] == 0:
        #         for col in range(len(matrix[0])):
        #             matrix[row][col] = 0
        # for col in range(len(matrix[0])):
        #     if matrix[0][col] == 0:
        #         for row in range(len(matrix)):
        #             matrix[row][col] = 0


        # for row in range(len(matrix)):
        #     if matrix[row][0] == 0:
        #         zero_row.append(row)
        # for col in range(len(matrix[0])):
        #     if matrix[0][col] == 0:
        #         zero_col.append(col)


        for i in zero_row:
            for col in range(len(matrix[0])):
                matrix[i][col] = 0
        for j in zero_col:
            for row in range(len(matrix)):
                matrix[row][j] = 0