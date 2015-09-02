__author__ = 'Simon'
# import collections
class Solution(object):
    def removeDuplicates(self, nums):
        # c = collections.Counter(nums)
        # result = c.keys()
        # return len(result)

        # result = list()
        # for i in range(len(nums)):
        #     if nums[i] not in result:
        #         result.append(nums[i])
        # return len(result)

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        num = 0
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                num = num +1
                nums[num] = nums[i+1]
        return num + 1