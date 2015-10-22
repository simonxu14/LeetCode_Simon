__author__ = 'Simon'
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        OPT = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(t)+1):
            OPT[0][i] = 0
        for j in range(len(s)+1):
            OPT[j][0] = 1
        OPT[0][0] = 1
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if s[j-1] != t[i-1]:
                    OPT[j][i] = OPT[j-1][i]
                else:
                    OPT[j][i] = OPT[j-1][i] + OPT[j-1][i-1]
        return OPT[len(s)][len(t)]