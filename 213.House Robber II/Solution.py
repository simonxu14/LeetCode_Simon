__author__ = 'Simon'
class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) < 4:
    #         return max(nums)
    #     nums = nums + nums
    #     sum = [0 for i in range(len(nums) + 1)]
    #     sum[0] = 0
    #     sum[1] = nums[0]
    #     for i in range(2, len(nums) +1):
    #         sum[i] = max(sum[i-1], sum[i-2]+nums[i-1])
    #
    #
    #     mid = len(nums)/2
    #     number1 = sum[mid-1]
    #     number2 = sum[len(nums)] - number1
    #     if number1 > number2:
    #         return number2
    #     else:
    #         return number1
    #
    def rob(self, nums):

        if len(nums) == 1: return nums[0]
        (last1, now1) = self.rob_non_circular(nums[1:] )
        (last2, now2) = self.rob_non_circular(nums)
        return max(now1, last2)

    def rob_non_circular(self, nums):

        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return last, now