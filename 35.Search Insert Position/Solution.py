__author__ = 'Simon'
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            else:
                if target < nums[i] and i == 0:
                    return 0
                if i < len(nums)-1 and target > nums[i] and target < nums[i+1]:
                    return i+1
                if i == len(nums)-1 and target > nums[i]:
                    return len(nums)
        return 0
