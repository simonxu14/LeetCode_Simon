__author__ = 'Simon'
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # dict = {}
        # current = []
        # for i in range(len(nums)):
        #     if nums[i] not in dict.keys():
        #         dict.fromkeys(nums[i], current.append(i))
        #     else:
        #         current = dict.get(nums[i])
        #         current.append(i)
        #         dict.update(nums[i], current)
        # for key in dict.keys():
        #     current = dict.get(nums[i])
        #     for m in range(len(current)-1):
        #         if current[m + 1] -
        #

        dict = {}
        for i, v in enumerate(nums):
            if v in dict and i - dict[v] <= k:
                return True
            dict[v] = i
        return False