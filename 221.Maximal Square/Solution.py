__author__ = 'Simon'
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        s = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        Max = 0
        for col in range(len(matrix[0])):
            s[0][col] = int(matrix[0][col])
            if s[0][col] > Max:
                Max = s[0][col]
        for row in range(len(matrix)):
            s[row][0] = int(matrix[row][0])
            if s[row][0] > Max:
                Max = s[row][0]

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if int(matrix[row][col]) == 0:
                    s[row][col] = 0
                else:
                    s[row][col] = min(s[row-1][col-1], s[row-1][col], s[row][col-1]) + 1
                    if s[row][col] > Max:
                        Max = s[row][col]
        return Max * Max