__author__ = 'Simon'
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set = {}
        # for i in range(len(nums)):
        #     if nums[i] not in set.keys():
        #         set[nums[i]] = 1
        #     else:
        #         set[nums[i]] += 1
        # for j in set.keys():
        #     if set[j] != 3:
        #         return j


        # a = set(nums)
        # a = sum(a)*3 -sum(nums)
        # a = a/2
        # return a

        ones, twos, threes = 0,0,0
        for item in nums:
            twos |= ones&item      #hold item which occur twice
            ones ^= item           #hold item which occur once
            threes = ones&twos     #hold item which occur three times

            ones ^= threes         #once some item occur three items, reset ones
            twos ^= threes         #once some item occur three items, reset twos
        return ones