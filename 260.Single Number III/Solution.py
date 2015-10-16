__author__ = 'Simon'
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic, res = {}, []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for k, v in dic.items():
            if v == 1:
                res.append(k)
        return res