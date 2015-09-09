__author__ = 'Simon'
class Solution(object):
    def canJump(self, nums):
        length = len(nums)
        maxine = 0
        for i in range(length):
            if i > maxine or maxine >= length-1:
                break
            maxine = max(maxine, i+nums[i])
        return maxine >= length -1