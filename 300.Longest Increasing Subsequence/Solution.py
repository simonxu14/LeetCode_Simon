from sys import maxint

__author__ = 'Simon'
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        amount = [0 for i in range(len(nums))]
        amount[0] = 1
        for i in range(1, len(nums)):



            # while j >= 0:
            #     if j == 0:
            #         if nums[j] < nums[i]:
            #             amount[i] = 2
            #             break
            #         else:
            #             amount[i] = 1
            #             break
            #     if nums[j] < nums[i]:
            #         amount[i] = amount[j] + 1
            #     j -= 1



            # max = -maxint
            # index = j
            # for j in range(i-1):
            #     if nums[j] < nums[i]:
            #         if nums[j] > max:
            #             max = nums[j]
            #             index = j
            # if max == -maxint:
            #     amount[i] = 1
            # else:
            #     amount[i] = amount[index] + 1
            index = i
            for j in range(i):
                if nums[j] < nums[i]:
                    if amount[j] > amount[index]:
                        index = j
            if index == i:
                amount[i] = 1
            else:
                amount[i] = amount[index]+1


        max_number = 0
        for i in range(len(amount)):
            if amount[i] > max_number:
                max_number = amount[i]
        return max_number