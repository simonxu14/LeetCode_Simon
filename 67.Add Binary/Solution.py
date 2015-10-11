__author__ = 'Simon'
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == "0":
            return b
        if b == "0":
            return a
        str = ""
        i = len(a) - 1
        j = len(b) - 1
        k = 0
        while i >= 0 and j >= 0:
            if int(a[i]) + int(b[j]) + k == 0:
                str = "0" + str
            elif int(a[i]) + int(b[j]) + k == 1:
                str = "1" + str
                if k == 1:
                    k = 0
            elif int(a[i]) + int(b[j]) + k == 2:
                str = "0" + str
                k = 1
            elif int(a[i]) + int(b[j]) + k == 3:
                str = "1" + str
                k = 1
            i -= 1
            j -= 1
        if i != -1:
            while i >= 0:
                if int(a[i]) + k == 0:
                    str = "0" + str
                if int(a[i]) + k == 1:
                    str = "1" + str
                    if k == 1:
                        k = 0
                if int(a[i]) + k == 2:
                    str = "0" + str
                    k = 1
                i -= 1
        if j != -1:
            while j >= 0:
                if int(b[j]) + k == 0:
                    str = "0" + str
                if int(b[j]) + k == 1:
                    str = "1" + str
                    if k == 1:
                        k = 0
                if int(b[j]) + k == 2:
                    str = "0" + str
                    k = 1
                j -= 1
        if k == 1:
            str = "1" + str
            k = 0
        return str