__author__ = 'Simon'
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        for i in range(index, len(nums)):
            res.append(path+[nums[i]])
            # print path+[nums[i]]
            # print index
            self.dfs(nums, i+1, path+[nums[i]], res)