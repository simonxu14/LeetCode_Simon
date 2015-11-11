__author__ = 'Simon'
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        result.append([])
        nums.sort()
        self.DFS(nums, [], result)
        return result


    def DFS(self, nums, current, result):
        if len(nums) == 0:
            return
        for i in range(len(nums)):
            if current+[nums[i]] not in result:
                result.append(current+[nums[i]])
            self.DFS(nums[i+1:], current+[nums[i]], result)