from sys import maxint

__author__ = 'Simon'
class Solution(object):
    def minimumTotal(self, triangle):
        # size = len(triangle)
        # size_k = size
        # last_len = 1
        # while size_k == 0:
        #     size_k = size_k - last_len
        #     last_len += 1
        #
        # sum = [0 for i in range(size)]
        # layer = 2
        # index = 0
        # sum[0] = triangle[0]
        # for i in range(1, size):
        #     if index == 0:
        #         sum[i] = triangle[i] + sum[i-layer+1]
        #         index += 1
        #     if index == layer-1:
        #         sum[i] = triangle[i] + sum[i-layer]
        #         layer += 1
        #         index = 0
        #     else:
        #         sum[i] = triangle[i] + min(sum[i-layer], sum[i-layer+1])
        #         index += 1
        #
        # max = 0
        # for j in range(size-last_len, size):
        #     if sum[j] > max:
        #         max = sum[j]
        # return max


        size = len(triangle)
        last_len = len(triangle[size-1])
        sum = []
        sum.append(triangle[0][0])
        index = 1
        for i in range(1, size):
            for j in range(0, len(triangle[i])):
                if j == 0:
                    sum.append(triangle[i][j] + sum[index - i])
                    index = index + 1
                if j == len(triangle[i]) - 1:
                    sum.append(triangle[i][j] + sum[index - i - 1])
                    index = index + 1
                if j != 0 and j != len(triangle[i]) - 1:
                    sum.append(triangle[i][j] + min(sum[index - i], sum[index - i - 1]))
                    index = index + 1
        result = maxint
        print sum
        for k in range(index - last_len, len(sum)):
            if sum[k] < result:
                result = sum[k]
        return result
