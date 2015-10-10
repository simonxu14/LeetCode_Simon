__author__ = 'Simon'
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        current = ""
        map = {}
        j = 0
        index = ""
        for i in range(len(str)):
            if i == len(str)-1:
                current = current + str[i]
                # print "AAA" + current
                if j == len(pattern):
                    return False
                if current in map.keys():
                    index = map.get(current)
                    if pattern[j] != index:
                        return False
                else:
                    if pattern[j] in map.values():
                        return False
                    map[current] = pattern[j]
                j += 1
            elif str[i] == " ":
                # print "BBB" + current
                if j == len(pattern):
                    return False
                if current in map.keys():
                    index = map.get(current)
                    if pattern[j] != index:
                        return False
                else:
                    if pattern[j] in map.values():
                        return False
                    map[current] = pattern[j]
                j += 1
                current = ""
            else:
                current += str[i]
        if j < len(pattern):
            return False
        else:
            return True
