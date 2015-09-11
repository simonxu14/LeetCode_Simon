_author_ = 'Simon'
class Solution(object):
    def uniquePaths(self, m, n):
        sum = [[0 for col in range(n)] for row in range(m)]
        sum[0][0] = 0
        # if m == 1:
        #     return 1
        # if n == 1:
        #     return 1
        # sum[1][0] = 1
        # sum[0][1] = 1
        for row in range(0, n):
            sum[row][0] = 1
        for col in range(0, m):
            sum[0][col] = 1
        for col in range(1, m):
            for row in range(1, n):
                sum[row][col] = sum[row-1][col] + sum[row][col-1]
        return sum[m-1][n-1]