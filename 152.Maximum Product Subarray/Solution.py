__author__ = 'Simon'
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        currentMax = nums[0]
        currentMin = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            temp = currentMax
            currentMax = max(n, n*currentMax, n*currentMin)
            currentMin = min(n, n*tmp, n*currentMin)
            ans = max(ans, currentMax)
        return ans