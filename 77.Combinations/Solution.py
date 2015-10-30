__author__ = 'Simon'
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # ans = []
        # stack = []
        # x = 1
        # while True:
        #     l = len(stack)
        #     if l == k:
        #         ans.append(stack[:])
        #     if l == k or x > n - k + l + 1:
        #         if not stack:
        #             return ans
        #         x = stack.pop() + 1
        #     else:
        #         stack.append(x)
        #         x += 1
#
# if __name__ == '__main__':
#     S = Solution()
#     print S.combine(4,2)



    def combine(self, n, k):
        res = []
        self.dfs(xrange(1,n+1), k, 0, [], res)
        return res

    def dfs(self, nums, k, index, path, res):
        #if k < 0:  #backtracking
            #return
        if k == 0:
            res.append(path)
            return # backtracking
        for i in xrange(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)