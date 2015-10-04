__author__ = 'Simon'
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n >= 1 and n & (n-1) == 0