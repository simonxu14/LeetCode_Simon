__author__ = 'Simon'
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = []
        current = []
        row_num = 1

        while row_num <= numRows:
            for k in range(row_num):
                if k == 0:
                    current.append(1)
                elif k == row_num - 1:
                    current.append(1)
                else:
                    current.append(result[len(result)-1][k-1] + result[len(result)-1][k])
            result.append(current)
            current = []
            row_num += 1

        return result
