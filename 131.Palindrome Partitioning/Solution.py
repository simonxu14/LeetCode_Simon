__author__ = 'Simon'
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.DFS(s, [], result)
        return result



    def DFS(self, s, path, result):
        if not s:
            result.append(path)
        for i in range(1, len(s)+1):
            if self.isPar(s[:i]):
                self.DFS(s[i:], path+[s[:i]], result)

    def isPar(self, s):
        return s == s[::-1]
