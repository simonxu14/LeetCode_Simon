__author__ = 'Simon'
class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return len(nums)
        while val in nums:
            nums.remove(val)
        return len(nums)





S = Solution()
print S.removeElement([1, 0, -1, 0, -2, 2], 0)