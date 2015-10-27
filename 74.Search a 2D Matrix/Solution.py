__author__ = 'Simon'
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if len(matrix) == 1:
        #     for col in range(len(matrix[0])):
        #         if target == matrix[0][col]:
        #             return True
        #     return False
        # else:
        row = 0
        col = 0
        for row in range(len(matrix)-1):
            if target == matrix[row][0]:
                return True
            if target > matrix[row][0] and target < matrix[row+1][0]:
                break
        if target >= matrix[-1][0]:
            for col in range(len(matrix[0])):
                if target == matrix[-1][col]:
                    return True
        else:
            for col in range(len(matrix[0])):
                if target == matrix[row][col]:
                    return True
        return False
