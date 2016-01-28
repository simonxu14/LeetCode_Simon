class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """


        # str = ""
        # list = []
        # result = []
        # for i in range(0, len(s)-9):
        #     str = s[i:i+10]
        #     list.append(str)
        # # print list
        # for m in range(len(list)):
        #     for n in range(m+1, len(list)):
        #         if list[m] == list[n] and list[m] not in result:
        #             result.append(list[m])
        # return result

        str = ""
        list = {}
        result = []
        for i in range(0, len(s)-9):
            str = s[i:i+10]
            print list.keys()
            print list
            if str in list:
                list[str] += 1
                if list[str] == 2:
                    result.append(str)
            else:
                list[str] = 1
        return result





if __name__ == '__main__':
    s = Solution()
    print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCAAAAA")
