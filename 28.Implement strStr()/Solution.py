__author__ = 'Simon'
class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        if len(haystack) == 0 and len(needle) != 0:
            return -1
        if len(haystack) != 0 and len(needle) == 0:
            return 0
        index = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(haystack) >= len(needle) + i:
                    for j in range(len(needle)):
                        if haystack[i+j] != needle[j]:
                            index = 1
                    if index == 0:
                        return i
                    else:
                        index = 0
        return -1



