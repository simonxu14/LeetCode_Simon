__author__ = 'Simon'
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        v = 1
        for i in range(1, len(nums)):
            v = v * nums[i]
        output.append(v)
        for j in range(1, len(nums)):
            if nums[j] == 0:
                v = 1
                for i in range(0, len(nums)):
                    if i != j:
                        v = v * nums[i]
                output.append(v)
            else:
                output.append(output[len(output)-1]*(nums[j-1])/(nums[j]))
        return output