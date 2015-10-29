__author__ = 'Simon'
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        l = 0
        r = len(citations)
        while l != r:
            m = (l + r)/ 2
            if citations[m] == n - m:
                return n - m
            if citations[m] > n - m:
                r = m
            else:
                l = m + 1
        return n - l