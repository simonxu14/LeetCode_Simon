__author__ = 'Simon'
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        for k in range(0, 32):
            num *= 2
            if (n%2 == 1):
                num += 1
            n/=2
        return num
