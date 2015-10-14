__author__ = 'Simon'
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i <= j:
            m = i + (j - i) / 2
            if isBadVersion(m):
                j = m - 1
            else:
                i = m + 1

        return i
