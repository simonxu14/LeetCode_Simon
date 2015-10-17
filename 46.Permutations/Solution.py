import copy

__author__ = 'Simon'
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        current = []
        result = []
        self.DFS(nums, current, result)
        return result


    def DFS(self, nums, current, result):
        if len(nums) == 1:
            current.append(nums[0])
            result.append(current)
            return
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            temp2 = current + [nums[i]]
            result = self.DFS(temp, temp2, result)

            # current.append(nums[i])
            # index = nums[i]
            # nums.remove(nums[i])
            # self.DFS(nums, current, result)
            # nums.insert(i, index)
            # current.pop()
        return

if __name__ == '__main__':
    S = Solution()
    list = [1,0]
    print S.permute(list)