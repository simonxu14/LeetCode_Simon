__author__ = 'Simon'
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if int(s[0]) == 0:
                return 0
            else:
                return 1
        OPT = [0 for i in range(len(s)+1)]
        OPT[0] = 1
        if int(s[0]) == 0:
            OPT[1] = 0
        else:
            OPT[1] = 1
        for i in range(2, len(s)+1):
            if int(s[i-1]) == 0:
                if int(s[i-2]) == 0 or int(s[i-2]) >=3:
                    OPT[i] = 0
                else:
                    OPT[i] = OPT[i-2]
            elif int(s[i-2:i]) <= 26 and int(s[i-2:i]) >= 10:
                OPT[i] = OPT[i-2] + OPT[i-1]
            else:
                OPT[i] = OPT[i-1]
        return OPT[len(s)]
