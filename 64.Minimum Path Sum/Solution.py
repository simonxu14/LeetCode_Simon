__author__ = 'Simon'
class Solution(object):
    def minPathSum(self, grid):
        row_size = len(grid)
        col_size = len(grid[0])
        sum = [[0 for col in range(col_size)] for row in range(row_size)]
        sum[0][0] = grid[0][0]
        for col in range(1, col_size):
            sum[0][col] = sum[0][col-1] + grid[0][col]
        for row in range(1, row_size):
            sum[row][0] = sum[row-1][0] + grid[row][0]
        for col in range(1, col_size):
            for row in range(1, row_size):
                sum[row][col] = min(sum[row-1][col], sum[row][col-1]) + grid[row][col]
        return sum[row_size-1][col_size-1]
