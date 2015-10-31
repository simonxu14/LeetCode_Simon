__author__ = 'Simon'
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 0:
        #     return 0
        # tmp = 0
        # result = 0
        # amount = 0
        # for i in range(len(nums)):
        #     if i == 0:
        #         tmp = nums[i]
        #         amount = 1
        #
        #     elif i == len(nums)-1:
        #         if tmp == nums[i]:
        #             amount += 1
        #         else:
        #             if amount == 1:
        #                 result = result + 1
        #                 amount = 1
        #             else:
        #                 result = result + 2
        #                 amount = 1
        #
        #     elif tmp == nums[i]:
        #         amount += 1
        #
        #     else:
        #         if amount == 1:
        #             result = result + 1
        #         else:
        #             result = result + 2
        #         tmp = nums[i]
        #         amount = 1
        #
        # if amount == 1:
        #     result = result + 1
        # else:
        #     result = result + 2
        # return result



        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        tmp = 0
        amount = 0
        i = 0
        j = 0
        length = len(nums)-1
        while True:
            if j == 0:
                tmp = nums[0]
                amount = 1
            elif j == length:
                if nums[i] == tmp:
                    if amount == 1:
                        break
                    else:
                        del nums[i]
                        break
                else:
                    break
            elif nums[i] == tmp:
                if amount == 1:
                    amount = 2
                else:
                    del nums[i]
                    i -= 1
            else:
                tmp = nums[i]
                amount = 1
            j += 1
            i += 1
        return len(nums)