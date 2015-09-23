import collections

__author__ = 'Simon'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # c = collections.Counter(nums)
        # return list(c.elements())[0]
        nums.sort()
        return nums[len(nums)//2]