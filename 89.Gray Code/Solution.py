__author__ = 'Simon'
class Solution(object):
    def grayCode(self, n):
        # result = []
        # current = []
        # current.append('0')
        # current.append('1')
        # for i in range(1, n):
        #     result = []
        #     for m in range(0, len(current)):
        #         result.append('0' + current[m])
        #     for n in range(0, len(current)):
        #         result.append('1' + current[n])
        # result = current
        result = []
        result.append(0)
        j = 0
        for i in range(0, n):
            high = 1 << i
            long = len(result)
            j = long - 1
            while j >= 0:
                result.append(high + result[j])
                print high + result[j]
                j -= 1
        return result
