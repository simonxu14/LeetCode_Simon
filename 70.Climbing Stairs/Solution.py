__author__ = 'Simon'
class Solution(object):
    def climbStairs(self, n):
        sum = []
        sum.append(1)
        sum.append(1)
        for i in range(2, n+1):
            sum.append(sum[i-1] + sum[i-2])
        return sum[n]
