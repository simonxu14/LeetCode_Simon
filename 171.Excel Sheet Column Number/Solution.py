__author__ = 'Simon'
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        i = len(s) - 1
        while i >= 0:
            sum = sum + (ord(s[i]) - ord('A') + 1) * (26 ** (len(s) - i - 1))
            i -= 1
        return sum