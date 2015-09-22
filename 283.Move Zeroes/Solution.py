__author__ = 'Simon'
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        current = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[current] = nums[i]
                current += 1
            i += 1
        while current < len(nums):
            nums[current] = 0
            current += 1
        return