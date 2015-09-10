import sys
__author__ = 'Simon'

class Solution(object):
    def jump(self, nums):
        # length = len(nums)
        # maxine = 0
        # step = 0
        # for i in range(length):
        #     if i > maxine or maxine >= length - 1:
        #         break
        #     maxine = max(maxine, i + nums[i])
        #     if maxine != maxine:
        #         step += 1
        # if maxine >= length - 1:
        #     return step
        # else: return 0



        # minjump = [sys.maxint] * len(nums)
        # minjump[0] = 0
        # farest = 0
        # for i in range(len(nums)):
        #     farest = min(i + nums[i], len(nums) - 1)
        #     for j in range(i+1, farest+1):
        #         if minjump[j] > minjump[i] + 1:
        #             minjump[j] = minjump[i] + 1
        # return minjump[len(nums)-1]



        n, cur_max, next_max, steps = len(nums), 0, 0, 0
        for i in xrange(n):
            if i > cur_max:
                steps += 1
                cur_max = next_max
                if cur_max >= n: break
            next_max = max(next_max, nums[i] + i)
        return steps