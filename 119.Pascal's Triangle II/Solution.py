__author__ = 'Simon'
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        result = []
        current = []
        row_num = 1

        while row_num <= rowIndex:
            for k in range(row_num+1):
                if k == 0:
                    current.append(1)
                elif k == row_num:
                    current.append(1)
                else:
                    current.append(result[k-1] + result[k])
            result = current
            current = []
            row_num += 1

        return result
