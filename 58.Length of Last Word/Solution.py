__author__ = 'Simon'
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = s.split()
        if li:
            return len(li[-1])
        else:
            return 0