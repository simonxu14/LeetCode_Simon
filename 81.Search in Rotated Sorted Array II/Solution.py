__author__ = 'Simon'
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l)/2

            if nums[mid] == target:
                return True

            while l < mid and nums[l] == nums[mid]:
                l += 1

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # if nums[l] == nums[mid]:
            #     r = mid - 1
        return False