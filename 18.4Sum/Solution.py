__author__ = 'Simon'
class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        result = list()
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                m = j + 1
                n = len(nums) - 1
                while m < n:
                    sum = nums[i] + nums[j] + nums[m] + nums[n]
                    if sum == target:
                        if [nums[i], nums[j], nums[m], nums[n]] in result:
                            m += 1
                            n -= 1
                        else:
                            result.append([nums[i], nums[j], nums[m], nums[n]])
                            m += 1
                            n -= 1
                    if sum < target:
                        m += 1
                    elif sum > target:
                        n -= 1
        return result

S = Solution()
print S.fourSum([1, 0, -1, 0, -2, 2], 0)