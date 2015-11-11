from sys import maxint

__author__ = 'Simon'
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # begin = 0
        # end = len(nums)-1
        # left = 0
        # right = 0
        # while(begin > end):
        #     mid = end/2
        #     if nums[mid] == target:
        #         if mid > right:
        #             right = mid
        #         if mid < left:
        #             left = mid
        #
        #
        #     if nums[mid] > target:
        #         right = mid
        #     if nums[mid] < target:
        #         left = mid

        lmost = self.leftsearch(nums, target)
        rmost = self.rightsearch(nums, target)
        return[lmost, rmost]

    def leftsearch(self, A, tar):
        l = 0
        r = len(A)-1
        tarI = -1
        while l <= r:
            mid = (l+r)/2
            if A[mid] > tar:
                r = mid - 1
            elif A[mid] < tar:
                l = mid + 1
            else:
                tarI = mid
                r = mid - 1
        return tarI

    def rightsearch(self, A, tar):
        l = 0
        r = len(A)-1
        tarI = -1
        while l <= r:
            mid = (l+r)/2
            if A[mid] > tar:
                r = mid -1
            elif A[mid] <tar:
                l = mid + 1
            else:
                tarI = mid
                l = mid+1
        return tarI