__author__ = 'Simon'
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # stack = []
        # amount = 0
        # result = []
        # x = 1
        # while True:
        #     amount = len(stack)
        #     if amount == k and sum(stack) == n:
        #         result.append(stack[:])
        #     if amount == k or number > n - k + amount + 1:
        #         if not stack:
        #             return result
        #         number = stack.pop() + 1
        #     else:
        #         stack.append(number)
        #         number = number + 1

        res = []
        self.dfs(xrange(1,10), k, 0, [], res, n)
        return res

    def dfs(self, nums, k, index, path, res, n):
        #if k < 0:  #backtracking
            #return
        if k == 0 and sum(path) == n:
            res.append(path)
            return # backtracking
        for i in xrange(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res, n)