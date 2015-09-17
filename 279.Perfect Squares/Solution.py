# from sys import maxint
#
# __author__ = 'Simon'
# class Solution(object):
#     def numSquares(self, n):
#         # if n == 0:
#         #     return 0
#         # k = 1
#         # while k * k <= n:
#         #     k = k + 1
#         # k = k - 1
#         # index = 0
#         # while n != 0:
#         #     while n >= k * k:
#         #         n = n - k * k
#         #         index = index + 1
#         #     k = k - 1
#         # return index
#
#         if n == 0:
#             return 0
#         min = [ maxint for i in range(n + 1) ]
#         min[0] = 0
#         y = 1
#         while y * y <= n:
#             min[y * y] = 1
#             y = y + 1
#         for x in range(1, n + 1):
#             y = 1
#             while x + y * y <= n:
#                 if min[x + y * y] == maxint or min[x] + 1 < min[x + y * y]:
#                     min[x + y * y] = min[x] + 1
#                 y = y + 1
#         return min[n]

class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]



