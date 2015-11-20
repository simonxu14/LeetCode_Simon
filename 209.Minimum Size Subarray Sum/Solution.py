__author__ = 'Simon'
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        tempSum = 0
        minL = 0

        while right < len(nums):
            tempSum += nums[right]
            while tempSum >= s and left <= right:
                if minL > right - left + 1 or minL == 0:
                    minL = right - left + 1
                tempSum -= nums[left]
                left += 1
            right += 1

        return minL