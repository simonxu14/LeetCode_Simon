__author__ = 'Simon'
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == None:
            return []
        result = []
        string = ""
        i = 0

        while i < len(nums):
            begin = nums[i]
            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                i += 1
            end = nums[i]
            if begin == end:
                result.append(str(begin))
            else:
                result.append(str(begin) + "->" + str(end))
            i += 1
        return result