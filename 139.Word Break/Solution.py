__author__ = 'Simon'
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        db = [False] * (len(s)+1)
        db[0] = True
        for j in range(1, len(s)+1):
            for i in range(0, j):
                if db[i] and s[i:j] in wordDict:
                    db[j] = True
        return db[len(s)]