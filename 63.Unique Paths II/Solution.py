__author__ = 'Simon'
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        sum = [[0 for col in range(len(obstacleGrid[0]))] for row in range(len(obstacleGrid))]
        sum[0][0] = 0
        for row in range(0, len(obstacleGrid)):
            if obstacleGrid[row][0] == 1:
                    sum[row][0] = 0
                    break
            else:
                sum[row][0] = 1
        for col in range(0, len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 1:
                    sum[0][col] = 0
                    break
            else:
                sum[0][col] = 1
        for col in range(1, len(obstacleGrid[0])):
            for row in range(1, len(obstacleGrid)):
                if obstacleGrid[row][col] == 1:
                    sum[row][col] = 0
                else:
                    sum[row][col] = sum[row-1][col] + sum[row][col-1]
        return sum[len(obstacleGrid)-1][len(obstacleGrid[0])-1]