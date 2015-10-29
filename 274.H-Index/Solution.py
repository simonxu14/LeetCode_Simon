__author__ = 'Simon'
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # number = len(citations)
        # for i in range(len(citations)):
        #     if citations[i] == number:
        #         return number
        #     number -= 1
        # return number+1


        # if not citations:
        #     return 0
        # citations.sort()
        # citations.reverse()
        # for i in range(len(citations)):
        #     if citations[i] > i+1:
        #         continue
        #     else:
        #         return i
        # return len(citations)

        # result = 0
        # if not citations:
        #     return 0
        # citations.sort()
        # i = len(citations)-1
        # while i > 0:
        #     if citations[i] <= i+1:
        #         result = citations[i]
        # return result


        if not citations:
            return 0
        citations.sort()
        citations.reverse()
        for i in range(len(citations)):
            if citations[i] < i+1:
                return i
        return len(citations)