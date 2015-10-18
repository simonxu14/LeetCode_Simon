__author__ = 'Simon'
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        copy = []
        current = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                current.append(matrix[i][j])
            copy.append(current)
            current = []

        for i in range(len(copy)):
            for j in range(len(copy[0])):
                matrix[j][len(copy)-i-1] = copy[i][j]