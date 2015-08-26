__author__ = 'Simon'
# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         min_number = int()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     current = nums[i] + nums[j] + nums[k] - target
#                     if current == 0:
#                         return target
#                     elif abs(current) < abs(min_number):
#                         min_number = current
#         return min_number + target

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                print i, j, k
                if sum == target:
                    return sum
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
        return result

S = Solution()
print S.threeSumClosest([-1,2,1,-4], 1)