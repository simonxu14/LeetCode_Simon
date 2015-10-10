__author__ = 'Simon'
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "0"
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        i = 2
        current = [1, 1]
        k = []
        index = 0
        element = 0

        while i < n:
            k = current
            current = []
            index = 0
            element = 0
            for j in range(len(k)):
                if j == 0:
                    # print "AAA"
                    element = k[j]
                    index += 1
                elif j == len(k) - 1:
                    # print "BBB"
                    if k[j] == element:
                        # print "CCC"
                        current.append(index + 1)
                        current.append(element)
                    else:
                        # print "DDD"
                        current.append(index)
                        current.append(element)
                        current.append(1)
                        current.append(k[j])
                elif k[j] != element:
                    # print "EEE"
                    current.append(index)
                    current.append(element)
                    element = k[j]
                    index = 1
                else:
                    # print "FFF"
                    index += 1
            i += 1
        string = ""
        for m in range(len(current)):
            string += str(current[m])
        return string


