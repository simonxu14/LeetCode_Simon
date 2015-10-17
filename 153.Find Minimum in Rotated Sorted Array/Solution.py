__author__ = 'Simon'
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.BinarySearch(nums)


    def BinarySearch(self, nums):
        m = 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        else:
            m = len(nums)/2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            elif nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m] > nums[len(nums)-1]:
                return self.BinarySearch(nums[m+1:])
            else:
                return self.BinarySearch(nums[0:m])