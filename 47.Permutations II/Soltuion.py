__author__ = 'Simon'
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.DFS(nums, [], result)
        return result

    def DFS(self, nums,  current, result):
        if len(nums) == 0:
            if current not in result:
                result.append(current[:])
                return
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                self.DFS(nums[:i]+nums[i+1:], current+[nums[i]], result)