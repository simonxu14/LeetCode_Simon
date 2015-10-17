__author__ = 'Simon'
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums[0] != 0:
        #     return 0
        # for i in range(len(nums)-1):
        #     if nums[i+1] - nums[i] == 2:
        #         return i+1
        # return len(nums)
        n = len(nums)
        return n * (n+1)/2 - sum(nums)
