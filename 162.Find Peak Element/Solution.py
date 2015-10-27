__author__ = 'Simon'
class Solution(object):
    
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        return self.BS(nums)


    def BS(self, nums):
        if len(nums) == 1 or len(nums) == 2:
            return 0
        if len(nums) == 3:
            if nums[1] > nums[0] and nums[1] > nums[2]:
                return 1
            else:
                return 0

        half = len(nums)/2
        if nums[half] > nums[half-1] and nums[half] > nums[half+1]:
            return half
        else:
            one = self.BS(nums[:half])
            two = self.BS(nums[half+1:])
            if one == 0 and two == 0:
                return 0
            elif one != 0:
                return one
            else:
                return two




        # if len(nums) == 1:
        #     return 0
        # if len(nums) == 2:
        #     if nums[0] > nums[1]:
        #         return 0
        #     else:
        #         return 1
        # if len(nums) == 3:
        #     if nums[1] > nums[0] and nums[1] > nums[2]:
        #         return 1
        #     if nums[0] > nums[1]:
        #         return 0
        #     if nums[2] > nums[1]:
        #         return 2



        # def findPeakElement2(self, nums):
        #     l, r = 0, len(nums)-1
        #     while l < r:
        #         mid = l + (r-l)//2
        #         if nums[mid] > nums[mid+1]:
        #             r = mid
        #         else:
        #             l = mid + 1
        #     return l
